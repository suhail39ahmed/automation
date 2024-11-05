# TSV File Splitter

This script splits a large TSV (Tab-Separated Values) file into smaller chunks, making it easier to manage and process.

## Features
- Splits a TSV file into multiple smaller files based on a specified chunk size.
- Retains the header in each chunk for easy readability.

## Requirements
- Python 3.x

## Usage
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd tsv_splitter

Run the script with the name of the TSV file you want to split:

bash
Copy code
python split_tsv.py <filename.tsv>
The script will create chunks named <filename.tsv>_chunk_0.tsv, <filename.tsv>_chunk_1.tsv, etc., in the same directory.

Customization
You can modify the chunk_size parameter in the split_file function in split_tsv.py to change the maximum size of each chunk (default is 245 MB).

License
This project is licensed under the MIT License.

css
Copy code

### 3. `.gitignore`
Create a `.gitignore` file to ensure that temporary files and Python cache files are not uploaded to GitHub.

pycache/ *.pyc *.pyo *.pyd *.db *.sqlite3 *.log

markdown
Copy code

### Important Notes
1. **Documentation**: The README.md file provides clear instructions for users on how to use the script.
2. **Code Comments**: The script is well-commented to explain its functionality, making it easier for others to understand and modify.
3. **Error Handling**: The script checks for the presence of the file and provides usage instructions if the script is not run with the correct arguments.

### Uploading to GitHub
1. Initialize a Git repository in the `tsv_splitter` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add TSV file splitter script"
Create a new repository on GitHub and follow the instructions to push your local repository to GitHub:
bash
Copy code
git remote add origin <your_github_repository_url>
git branch -M main
git push -u origin main