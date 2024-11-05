# Key Vault Secret Copier

This script copies secrets from one Azure Key Vault to another. It retrieves all secrets from a source Key Vault and stores them in a new Key Vault, making it useful for managing secrets across different environments or subscriptions.

## Features
- Fetches all secrets from a specified source Azure Key Vault.
- Copies those secrets to a new Azure Key Vault.
- Outputs confirmation of each secret copied.

## Requirements
- Python 3.x
- Azure SDK for Python (`azure-identity` and `azure-keyvault-secrets`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd keyvault-secret-copier
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
Run the script by providing the names of the new Key Vault and the destination Key Vault:

bash
Copy code
python keyvault_secret_copier.py <new_keyvault_name> <destination_keyvault_name>
The script will output the names of secrets copied to the new Key Vault.

Important Notes
Ensure you have the necessary Azure permissions to access both Key Vaults.
The script uses DefaultAzureCredential for authentication, which requires proper authentication setup (e.g., environment variables, managed identity).
License
This project is licensed under the MIT License.

csharp
Copy code

### Uploading to GitHub
1. Initialize a Git repository in the `keyvault-secret-copier` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add Azure Key Vault secret copier script"
Create a new repository on GitHub and follow the instructions to push your local repository to GitHub:
bash
Copy code
git remote add origin <your_github_repository_url>
git branch -M main
git push -u origin main
This structure and documentation ensure that your project is well-organized, easy to understand, and ready for public use on GitHub.






