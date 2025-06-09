import requests

def get_github_issues(repo_url):
    try:
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    except Exception as e:
        print("Invalid repo URL")
        return []

    response = requests.get(api_url)
    
    if response.status_code != 200:
        print(f"Error fetching issues: {response.status_code}")
        return []
    
    issues = response.json()
    return [issue for issue in issues if 'pull_request' not in issue]
