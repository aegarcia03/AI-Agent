# 📰 Article-Summarizer AI Agent

This project is a **learning sandbox** for building AI agents in progressive steps — from a single-file Python script to a modular multi-agent system using [CrewAI].

I’m a junior software engineer, so the goal is to keep things simple, well-commented, and easy to extend.

---

## 📐 Project Structure (so far)


---article-summarizer/
├── venv/ # Python virtual-env (not tracked in Git)
├── summarizer.py # Step 1: basic agent (requests + BeautifulSoup + OpenAI)
├── .env.example # Copy to .env and paste your OpenAI key


## 🔗 Step 1 – “Hello Agent”

* **Tech**: Python 3.12, `requests`, `beautifulsoup4`, `python-dotenv`, `openai`
* **What it does**:  
  1. Fetches raw HTML from a URL  
  2. Strips scripts/styles, keeps visible text (≤3 kB)  
  3. Sends that text to the OpenAI Chat API and prints a plain-English summary

Run it:

```bash
# clone + enter + create env
git clone https://github.com/aegarcia03/AI_Agent.git
cd article-summarizer
python -m venv venv && source venv/bin/activate

# install deps & set your key
pip install -r requirements.txt
cp .env.example .env     # then edit .env and paste your OPENAI_API_KEY

python summarizer.py
```

🚀 Step 2 – “CrewAI Upgrade” (WIP)
Planned next milestone:

Tech additions: crewai, langchain, maybe a vector DB (Chroma)

Agents

Crawler – collects full article text & metadata

Summarizer – condenses the article

Refiner – polishes tone or length per user prompt
