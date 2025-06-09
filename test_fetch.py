from github_fetcher import get_github_issues
from ai_summarizer import summarize_issue

repo = input("Enter GitHub repo URL (e.g., https://github.com/vercel/next.js): ").strip()
issues = get_github_issues(repo)

if not issues:
    print("No issues found.")
else:
    for i, issue in enumerate(issues[:3], 1):  # Limit to 3 to avoid token limits
        title = issue['title']
        body = issue.get('body', '')
        print(f"\n{i}. {title}")
        print(f"URL: {issue['html_url']}")
        summary = summarize_issue(title, body)
        print(summary)
        print("-" * 60)
