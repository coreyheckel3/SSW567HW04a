import requests
import json

def gitApi(ID):
    repos = requests.get(f"https://api.github.com/users/{ID}/repos")

    if repos.status_code != 200:
        print("User ID does not exist")
        return False
    repos = repos.json()
    if len(repos) == 0:
        print("User has no repositories")
        return False

    for repo in repos:
        repoName = repo['name']
        commits = requests.get(f"https://api.github.com/repos/{ID}/{repoName}/commits")

        if commits.status_code == 200:
            commits = commits.json()
            commitCount = len(commits)
            print(f"Repository: {repoName}, Commits: {commitCount}")
        else:
            print(f"Error fetching commits: {repoName}")

    return True

gitApi("coreyheckel3")