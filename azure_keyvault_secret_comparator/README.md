# Key Vault Secret Comparator

This script compares secrets stored in two Azure Key Vaults and identifies differences between them. It fetches secrets from both Key Vaults and prints out any discrepancies in their values.

## Features
- Fetches and compares secrets from two Azure Key Vaults.
- Outputs any differences found between the two Key Vaults.

## Requirements
- Python 3.x
- Azure SDK for Python (`azure-identity` and `azure-keyvault-secrets`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd keyvault-secret-comparator
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Usage
Run the script by providing the names of the source and destination Key Vaults:

bash
Copy code
python keyvault_secret_comparator.py <source_keyvault_name> <destination_keyvault_name>
The script will output any differences found between the two Key Vaults.

Important Notes
Ensure that you have the appropriate Azure permissions to access the Key Vaults.
The script uses DefaultAzureCredential which requires proper authentication setup (e.g., environment variables, managed identity).
License
This project is licensed under the MIT License.

csharp
Copy code

### Uploading to GitHub
1. Initialize a Git repository in the `keyvault-secret-comparator` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add Azure Key Vault secret comparator script"
Create a new repository on GitHub and follow the instructions to push your local repository to GitHub:
bash
Copy code
git remote add origin <your_github_repository_url>
git branch -M main
git push -u origin main
This structure provides clarity and usability for anyone who wants to use your script while maintaining good coding practices and documentation.