# GitHub Issue Summarizer AI Agent

This is a mini AI agent that fetches open issues from any public GitHub repository, summarizes each issue using GPT-4, and classifies it (Bug / Feature / Question / Other). It helps developers quickly understand and prioritize issues in large open-source projects.


---

## What It Does

- Accepts a public GitHub repository URL as user input
- Fetches open issues using the GitHub API
- Uses OpenAI’s GPT to summarize and classify each issue
- Displays results directly in the terminal

---

## Tech Stack

| Tool         | Purpose                            |
|--------------|-------------------------------------|
| **Python**   | Core programming language           |
| **GitHub API** | To access public issue data       |
| **OpenAI API (GPT-4)** | Summarizing and classifying issues |
| **CLI (Terminal)** | User interface                |

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/amoghastagi/github-ai-agent.git
cd github-ai-agent
```

### 2. Set Up Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install openai requests
```

### 3. Add Your OpenAI API Key

In `ai_summarizer.py`, replace:

```python
client = openai.OpenAI(api_key="YOUR_OPENAI_KEY")
```

With your actual API key from https://platform.openai.com/account/api-keys

### 4. Run the Agent

```bash
python test_fetch.py
```

Enter a public GitHub repo URL when prompted (e.g. `https://github.com/vercel/next.js`)

---

## Sample Output

```
1. Feature: Add dark mode
URL: https://github.com/...
Summary: The issue is a request for dark mode support in the UI, which users say would improve accessibility and reduce eye strain.
Type: Feature
------------------------------------------------------------

2. Bug: App crashes on load
URL: https://github.com/...
Summary: Describes an app crash when opened on iOS. Likely due to a recent navigation change.
Type: Bug
------------------------------------------------------------
```

---

## Why This Is Useful

GitHub repositories often contain dozens or hundreds of open issues. This agent:
- Helps developers read and understand issues faster
- Automatically classifies issues
- Acts like a smart assistant for triaging bugs and features

---

## If I Had More Time...

- Add support for exporting summaries to a file (Markdown or CSV)
- Create a web UI using Streamlit
- Allow automatic prioritization of issues
- Add filtering (e.g. only bugs, or only high-priority issues)

---

## License

MIT License — free to use, modify, and share.

---

## Author

**Amogh Astagi**  
[LinkedIn](https://www.linkedin.com/in/amoghastagi) • [GitHub](https://github.com/amoghastagi)