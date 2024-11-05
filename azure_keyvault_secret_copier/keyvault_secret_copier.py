from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import sys

def get_all_secrets(vault_url, credential):
    """
    Retrieve all secrets from the specified Azure Key Vault.

    :param vault_url: URL of the Azure Key Vault.
    :param credential: DefaultAzureCredential object for authentication.
    :return: A dictionary of secret names and their values.
    """
    client = SecretClient(vault_url=vault_url, credential=credential)
    secrets = client.list_properties_of_secrets()
    secret_values = {}

    for secret in secrets:
        secret_name = secret.name
        secret_bundle = client.get_secret(secret_name)
        secret_values[secret_name] = secret_bundle.value

    return secret_values

def copy_secrets_to_new_keyvault(secrets, vault_url, credential):
    """
    Copy secrets to a new Azure Key Vault.

    :param secrets: A dictionary of secrets to copy.
    :param vault_url: URL of the new Azure Key Vault.
    :param credential: DefaultAzureCredential object for authentication.
    """
    client = SecretClient(vault_url=vault_url, credential=credential)
    
    for secret_name, secret_value in secrets.items():
        client.set_secret(secret_name, secret_value)
        print(f"Secret '{secret_name}' created in the new Key Vault.")

def main(new_keyvault_name, destination_keyvault_name):
    """
    Main function to copy secrets from one Azure Key Vault to another.

    :param new_keyvault_name: Name of the new Key Vault where secrets will be copied.
    :param destination_keyvault_name: Name of the source Key Vault from which secrets will be copied.
    """
    new_vault_url = f"https://{new_keyvault_name}.vault.azure.net/"
    destination_vault_url = f"https://{destination_keyvault_name}.vault.azure.net/"
    
    # Authenticate using DefaultAzureCredential
    credential = DefaultAzureCredential()

    # Get all secrets from the destination Key Vault
    source_secrets = get_all_secrets(destination_vault_url, credential)

    # Copy all secrets to the new Key Vault
    copy_secrets_to_new_keyvault(source_secrets, new_vault_url, credential)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python keyvault_secret_copier.py <new_keyvault_name> <destination_keyvault_name>")
        sys.exit(1)

    new_keyvault_name = sys.argv[1]
    destination_keyvault_name = sys.argv[2]

    main(new_keyvault_name, destination_keyvault_name)
