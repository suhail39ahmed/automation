# Azure Key Vault Upload Secrets

This repository contains a Python script for uploading secrets to Azure Key Vault from a CSV file.

## Prerequisites

- Python 3.x
- Azure SDK for Python:
  - `azure-identity`
  - `azure-keyvault-secrets`
- Azure subscription and access to the Key Vault

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/azure-keyvault-upload-secrets.git
   cd azure-keyvault-upload-secrets
Install the required packages:
bash
Copy code
pip install azure-identity azure-keyvault-secrets
Usage
Run the script with the following command:

bash
Copy code
python upload_secrets.py <key_vault_name> <csv_file_path>
Example
bash
Copy code
python upload_secrets.py kv-my-keyvault keyvault_secrets.csv
CSV File Format
The CSV file should have the following format:

csv
Copy code
Secret Name,Secret Value
my-secret-1,secret-value-1
my-secret-2,secret-value-2
License
This project is licensed under the MIT License - see the LICENSE file for details.

shell
Copy code

### .gitignore Content
pycache/ *.pyc *.pyo *.pyd .venv/ env/ venv/ *.env

vbnet
Copy code

### Final Steps to Create the Repository

1. **Create the Repository on GitHub**:
   - Go to GitHub and create a new repository named `azure-keyvault-upload-secrets`.
   - Set it to public.

2. **Initialize the Repository Locally**:
   In your terminal, navigate to the folder where you want to create your project and run:
   ```bash
   mkdir azure-keyvault-upload-secrets
   cd azure-keyvault-upload-secrets
   git init
Create the Files: Create the README.md, upload_secrets.py, and .gitignore files with the content provided above.

Follow the Git Commands: Use the Git commands to add, commit, and push your changes to the GitHub repository:

bash
Copy code
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/azure-keyvault-upload-secrets.git
git push -u origin main
This setup will provide a clear structure and documentation for your script, making it accessible and understandable for users who want to upload secrets to Azure Key Vault. If you need further modifications or additional features, feel free to ask!