import os, requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()             
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_text_from_url(url):
    html = requests.get(url, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return " ".join(soup.get_text(" ").split())[:3000]

def summarize_text(text):
    prompt = f"Summarize the following article in plain English:\n\n{text}"
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",        # or gpt-4o / gpt-4-turbo
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()

def summarize_url(url):
    print(f"🔗  Fetching: {url}")
    return summarize_text(get_text_from_url(url))

if __name__ == "__main__":
    url = input("Enter a URL to summarize: ")
    print("\n📄 Summary:\n")
    print(summarize_url(url))
