import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_issue(title, body):
    prompt = f"""
You are an AI GitHub assistant. A user has asked you to summarize and classify a GitHub issue.

Issue Title: {title}
Issue Body: {body}

Respond in this format:
Summary: ...
Type: (Bug / Feature / Question / Other)
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
