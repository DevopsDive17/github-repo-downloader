
# GitHub Repo Downloader
A simple Python script to download all public GitHub repositories for any user or organization.

## Features
- **Download All Repositories**: Fetches all public repositories for a specified user or organization.
- **Update Existing Repositories**: Automatically pulls updates if the repository already exists locally.
- **Pagination Support**: Handles large repositories with seamless pagination.
- **Minimal Dependencies**: Requires only `requests` and `git`.

---

## Requirements
- Python 3.7+
- `requests` library (`pip install requests`)
- Git installed and configured (`git --version` should work)

---

##  Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/github-repo-downloader.git
   cd github-repo-downloader
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

---

##  Usage
1. Run the script:
   ```bash
   python github_downloader.py
   ```

2. Enter the requested information:
   - **GitHub username** → The user or organization whose repos you want to download.
   - **GitHub personal access token** → Optional, but recommended to avoid rate limits.

3. All repositories will be downloaded to `./my-github-repos` by default.

---

## 💡 Example Output
```
===== GitHub Repository Downloader =====

GitHub Username: octocat
GitHub Token (optional, press Enter to skip): 

Saving repositories to: ./my-github-repos

Fetching repositories for octocat...

Found 8 repositories to download

[1/8] Hello-World
Cloning new repository...
✓ Successfully cloned Hello-World

[2/8] Spoon-Knife
Cloning new repository...
✓ Successfully cloned Spoon-Knife

...

✓ Complete! All 8 repositories downloaded to ./my-github-repos
```

---

## Creating a GitHub Token (Optional)
While the script works without a token, GitHub limits the number of API requests for unauthenticated users.  
To create a token:
1. Go to **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**.
2. Click **Generate new token**.
3. Give it a name and select the **public_repo** scope (or **repo** for private repositories).
4. Click **Generate token** and copy the token.

---

## Troubleshooting
- If you encounter `Rate Limit Exceeded`, try adding a GitHub Token.
- Make sure `git` is installed and accessible from your terminal.

---

## Contributing
Feel free to submit issues or pull requests if you find any bugs or want to add features.

---

## License
MIT License - Feel free to use, share, and modify this script.

---
