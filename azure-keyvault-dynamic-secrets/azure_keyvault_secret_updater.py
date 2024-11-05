import argparse
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError
from azure.mgmt.databricks import AzureDatabricksManagementClient
from azure.mgmt.eventhub import EventHubManagementClient

def get_databricks_workspace_url(subscription_id, resource_group_name, workspace_name):
    """
    Get the URL of the Databricks workspace.
    """
    credential = DefaultAzureCredential()
    databricks_client = AzureDatabricksManagementClient(credential, subscription_id)
    workspace = databricks_client.workspaces.get(resource_group_name, workspace_name)
    return workspace.workspace_url

def get_event_hub_primary_key(subscription_id, resource_group_name, namespace_name, event_hub_name, sas_policy_name):
    """
    Get the primary access key for the specified Event Hub.
    """
    credential = DefaultAzureCredential()
    eventhub_client = EventHubManagementClient(credential, subscription_id)
    access_keys = eventhub_client.event_hubs.list_keys(
        resource_group_name,
        namespace_name,
        event_hub_name,
        sas_policy_name
    )
    return access_keys.primary_key

def create_or_update_secret(key_vault_name, secrets_dict, subscription_id, resource_group_name, workspace_name, event_hub_name, namespace_name, sas_policy_name):
    """
    Create or update secrets in the Azure Key Vault.
    """
    credential = DefaultAzureCredential()
    key_vault_url = f"https://{key_vault_name}.vault.azure.net/"
    client = SecretClient(vault_url=key_vault_url, credential=credential)

    for secret_name in secrets_dict.keys():
        try:
            # Disable existing secret if it exists
            existing_secret = client.get_secret(secret_name)
            client.update_secret_properties(existing_secret.name, enabled=False)
            print(f"Secret '{secret_name}' disabled in {key_vault_name}.")
        except ResourceNotFoundError:
            # If the secret does not exist, proceed to create it
            pass
        except Exception as e:
            print(f"Failed to disable secret '{secret_name}' in {key_vault_name}: {e}")
            continue

        # Set the secret value based on the secret name
        if secret_name == "dems-dbw-workspace-url":
            secret_value = get_databricks_workspace_url(subscription_id, resource_group_name, workspace_name)
        elif secret_name == "dems-evh-rea-aue-01-shared-access-key-secret":
            secret_value = get_event_hub_primary_key(subscription_id, resource_group_name, namespace_name, event_hub_name, sas_policy_name)
        else:
            secret_value = secrets_dict[secret_name]

        client.set_secret(secret_name, secret_value)
        print(f"Secret '{secret_name}' set successfully in {key_vault_name}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update multiple secrets in an Azure Key Vault.")
    parser.add_argument("new_keyvault_name", help="Name of the new Key Vault.")
    parser.add_argument("subscription_id", help="Azure Subscription ID.")
    parser.add_argument("resource_group_name", help="Resource Group Name.")
    parser.add_argument("workspace_name", help="Databricks Workspace Name.")
    parser.add_argument("event_hub_name", help="Event Hub Name.")
    parser.add_argument("namespace_name", help="Event Hub Namespace Name.")
    parser.add_argument("sas_policy_name", help="Event Hub SAS Policy Name.")
    parser.add_argument("--secrets", required=True, nargs='+', help="List of additional secrets in the format name=value.")
    
    args = parser.parse_args()
    
    # Convert the list of secrets to a dictionary
    secrets_dict = dict(secret.split('=') for secret in args.secrets)
    
    # Update secrets in the Key Vault
    create_or_update_secret(args.new_keyvault_name, secrets_dict, args.subscription_id, args.resource_group_name, args.workspace_name, args.event_hub_name, args.namespace_name, args.sas_policy_name)
