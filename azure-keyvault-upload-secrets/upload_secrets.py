import csv
import sys
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError

def upload_secrets_to_key_vault(key_vault_name, csv_file_path):
    # Construct the Key Vault URL
    vault_url = f"https://{key_vault_name}.vault.azure.net"
    
    # Initialize SecretClient
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)

    # Read secrets from CSV file and upload to Key Vault
    try:
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                secret_name = row['Secret Name']
                secret_value = row['Secret Value']
                
                # Upload the secret to Key Vault
                client.set_secret(secret_name, secret_value)
                print(f"Uploaded secret: {secret_name}")

    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except ResourceNotFoundError:
        print(f"Error: Key Vault '{key_vault_name}' does not exist.")
    except HttpResponseError as e:
        print(f"HTTP error: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python upload_secrets.py <key_vault_name> <csv_file_path>")
        sys.exit(1)

    key_vault_name = sys.argv[1]
    csv_file_path = sys.argv[2]

    upload_secrets_to_key_vault(key_vault_name, csv_file_path)
    print("Secrets uploaded successfully.")
