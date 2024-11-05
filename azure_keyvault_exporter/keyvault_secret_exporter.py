import csv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError
import os

def export_secrets_to_csv(key_vault_name, csv_file):
    """
    Export secrets from Azure Key Vault to a CSV file.

    :param key_vault_name: Name of the Azure Key Vault.
    :param csv_file: Path to the CSV file where secrets will be saved.
    """
    key_vault_url = f"https://{key_vault_name}.vault.azure.net"
    
    # Authenticate to Azure
    credential = DefaultAzureCredential()
    
    # Create a secret client
    client = SecretClient(vault_url=key_vault_url, credential=credential)

    print("Downloading secrets from Azure Key Vault...")
    try:
        all_secrets = client.list_properties_of_secrets()
        
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Secret Name', 'Secret Value'])
            
            for secret in all_secrets:
                # Get the secret value
                secret_bundle = client.get_secret(secret.name)
                secret_name = secret_bundle.name
                secret_value = secret_bundle.value
                
                # Write to CSV file
                writer.writerow([secret_name, secret_value])
                print(f"Secret Name: {secret_name} exported.")
        
        print(f"Secrets downloaded successfully to {csv_file}")

    except ResourceNotFoundError:
        print(f"Failed to retrieve secrets from {key_vault_name}. Please check the vault name and credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    key_vault_name = os.getenv('AZURE_KEY_VAULT_NAME', 'kv-rea-dev-dems-aue-01')  # Use an environment variable for flexibility
    csv_file = 'keyvault_secrets.csv'
    export_secrets_to_csv(key_vault_name, csv_file)
