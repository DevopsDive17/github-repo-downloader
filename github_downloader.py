#!/usr/bin/env python3
"""
Simple GitHub Repository Backup Script
Downloads all repositories for a GitHub user with minimal configuration.
"""
import os
import subprocess
import requests
import getpass

def main():
    # Get user inputs
    username = input("Enter your GitHub username: ").strip()
    token = getpass.getpass("Enter your GitHub token (press Enter to skip): ").strip()
    backup_dir = input("Enter backup directory (default: ./github_repos): ").strip()
  
    # Set defaults
    if not backup_dir:
        backup_dir = "./github_repos"
    
    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)
    print(f"Backing up to: {os.path.abspath(backup_dir)}")
    
    # Set up session with authentication if token provided
    session = requests.Session()
    if token:
        session.headers.update({'Authorization': f'token {token}'})
    
    # Get all repositories (personal + from organizations)
    all_repos = []
    
    # Get user's repositories
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        response = session.get(url)
        
        if response.status_code != 200:
            print(f"Error accessing GitHub API: {response.status_code}")
            print(response.text)
            return
        
        repos = response.json()
        if not repos:
            break
            
        all_repos.extend(repos)
        page += 1
    
    # Get repositories from organizations
    try:
        if token:
            orgs_url = "https://api.github.com/user/orgs"
        else:
            orgs_url = f"https://api.github.com/users/{username}/orgs"
            
        orgs_response = session.get(orgs_url)
        orgs_response.raise_for_status()
        
        for org in orgs_response.json():
            org_name = org['login']
            page = 1
            
            while True:
                org_repos_url = f"https://api.github.com/orgs/{org_name}/repos?page={page}&per_page=100"
                org_repos_response = session.get(org_repos_url)
                org_repos_response.raise_for_status()
                
                org_repos = org_repos_response.json()
                if not org_repos:
                    break
                    
                all_repos.extend(org_repos)
                page += 1
    except requests.RequestException as e:
        print(f"Warning: Could not fetch organization repositories: {e}")
    
    # Clone or update repositories
    total = len(all_repos)
    print(f"Found {total} repositories to back up")
    
    for i, repo in enumerate(all_repos, 1):
        repo_name = repo['name']
        repo_url = repo['clone_url']
        repo_path = os.path.join(backup_dir, repo_name)
        
        print(f"[{i}/{total}] Processing {repo_name}...")
        
        if os.path.exists(repo_path):
            # Update existing repository
            print(f"Updating {repo_name}...")
            try:
                subprocess.run(
                    ["git", "pull"],
                    cwd=repo_path,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print(f"✓ Updated {repo_name}")
            except subprocess.CalledProcessError:
                print(f"✗ Failed to update {repo_name}")
        else:
            # Clone new repository
            print(f"Cloning {repo_name}...")
            try:
                subprocess.run(
                    ["git", "clone", repo_url, repo_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                print(f"✓ Cloned {repo_name}")
            except subprocess.CalledProcessError:
                print(f"✗ Failed to clone {repo_name}")
    
    print(f"\nBackup complete! All repositories saved to {os.path.abspath(backup_dir)}")

if __name__ == "__main__":
    main()
