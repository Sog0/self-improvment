from google import genai
import os

client = genai.Client()

with open("README.md", "r") as f:
    content = f.read()

prompt = f"""
Improve the content of this repository. Add one sentence to improve story. Return only extended text for file.

{content}
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=prompt
)

with open("README.md", "r+") as f:
    f.write(response.text)