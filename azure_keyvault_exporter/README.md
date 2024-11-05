# Azure Key Vault Secret Exporter

This script exports all secrets from an Azure Key Vault to a CSV file. It retrieves the secret names and their values and saves them in a structured format, making it easy to manage and review your secrets.

## Features
- Downloads all secrets from a specified Azure Key Vault.
- Exports secrets to a CSV file.
- Handles errors gracefully and provides meaningful messages.

## Requirements
- Python 3.x
- Azure SDK for Python (`azure-identity` and `azure-keyvault-secrets`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd keyvault-secret-exporter
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
Set the environment variable for the Azure Key Vault name or modify the script to specify the vault name directly. Then run the script:

bash
Copy code
python keyvault_secret_exporter.py
This will create a keyvault_secrets.csv file containing all the secrets from the specified Azure Key Vault.

Important Notes
Ensure you have the necessary Azure permissions to access the Key Vault.
Be cautious when handling exported secrets, especially in shared environments.
License
This project is licensed under the MIT License.

csharp
Copy code

### Uploading to GitHub
1. Initialize a Git repository in the `keyvault-secret-exporter` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add Azure Key Vault secret exporter script"
Create a new repository on GitHub and follow the instructions to push your local repository to GitHub:
bash
Copy code
git remote add origin <your_github_repository_url>
git branch -M main
git push -u origin main