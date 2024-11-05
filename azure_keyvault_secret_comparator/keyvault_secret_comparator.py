import os
import sys
import argparse
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from collections import defaultdict

def get_key_vault_secrets(vault_url):
    """
    Fetch all secrets from the specified Azure Key Vault.

    :param vault_url: URL of the Azure Key Vault.
    :return: A dictionary of secret names and their values.
    """
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secrets = {}

    # Fetch secrets
    secret_properties = client.list_properties_of_secrets()
    for secret_property in secret_properties:
        secret_name = secret_property.name
        secret = client.get_secret(secret_name)
        secrets[secret_name] = secret.value

    return secrets

def compare_secrets(secrets1, secrets2):
    """
    Compare two dictionaries of secrets and identify differences.

    :param secrets1: First dictionary of secrets.
    :param secrets2: Second dictionary of secrets.
    :return: A dictionary of differences.
    """
    all_keys = set(secrets1.keys()).union(set(secrets2.keys()))
    differences = defaultdict(dict)

    for key in all_keys:
        value1 = secrets1.get(key)
        value2 = secrets2.get(key)
        if value1 != value2:
            differences[key]['env1'] = value1
            differences[key]['env2'] = value2

    return differences

def main(source_vault_name, destination_vault_name):
    """
    Main function to compare secrets between two Azure Key Vaults.

    :param source_vault_name: Name of the source Key Vault.
    :param destination_vault_name: Name of the destination Key Vault.
    """
    source_vault_url = f"https://{source_vault_name}.vault.azure.net/"
    destination_vault_url = f"https://{destination_vault_name}.vault.azure.net/"

    # Get secrets from both Key Vaults
    secrets_env1 = get_key_vault_secrets(source_vault_url)
    secrets_env2 = get_key_vault_secrets(destination_vault_url)

    # Compare secrets
    differences = compare_secrets(secrets_env1, secrets_env2)

    # Output differences
    if differences:
        print("Differences found between the environments:")
        for key, diff in differences.items():
            print(f"Secret: {key}")
            print(f"  Source Vault: {diff['env1']}")
            print(f"  Destination Vault: {diff['env2']}")
    else:
        print("No differences found between the environments.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python keyvault_secret_comparator.py <source_keyvault_name> <destination_keyvault_name>")
        sys.exit(1)

    source_vault_name = sys.argv[1]
    destination_vault_name = sys.argv[2]
    
    main(source_vault_name, destination_vault_name)
