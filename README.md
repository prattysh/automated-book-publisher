# Automated Book Publisher (with AI + Human-in-the-loop Editing)

This project automates the end-to-end workflow of publishing chapters from classic books by combining AI rewriting, grammar polishing, human editing, and vector storage.

---

## Features

-  Web scraping from book chapter URLs (e.g., Wikisource)
-  AI-generated rewritten content (via Local LLM: Ollama)
-  AI Reviewer for grammar and flow improvements
-  Human Editor pass (rule-based or optionally LLM-assisted)
-  Stores final edited version in ChromaDB for semantic retrieval
-  Semantic search to retrieve refined content using queries

---

##  Architecture

```
┌────────────┐      ┌────────────┐      ┌────────────┐      ┌────────────┐
│  Scraper   ├─────▶│ AI Writer  ├─────▶│ AI Reviewer├─────▶│Human Editor│
└─────┬──────┘      └─────┬──────┘      └─────┬──────┘      └─────┬──────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
  Web Page           Rewritten          Grammar-Polished   Final Human-Checked
 (HTML)               Text                 Version             Version

                       ▼
               ┌──────────────┐
               │ ChromaDB Store│
               └──────┬───────┘
                      ▼
            Semantic Search Retrieval
```

---

##  Folder Structure

```
automated-book-publisher/
├── main.py                # Main pipeline script
├── scraper.py             # Scrapes and saves raw text & screenshot
├── ai_writer.py           # Rewrites text using local LLM (Ollama)
├── ai_reviewer.py         # Polishes grammar & style using LLM
├── human_editor.py        # Final human-style edits
├── chroma_store.py        # Save/retrieve from ChromaDB
├── outputs/               # Stores screenshots and text files
└── README.md              # Documentation
```

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/prattysh/automated-book-publisher.git
cd automated-book-publisher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright dependencies
playwright install

# 4. Make sure Ollama is running locally
ollama run llama3
```

---

## Usage

```bash
python main.py
```

The pipeline will:
- Scrape the raw chapter
- Rewrite it using a local LLM
- Review it with AI
- Apply human editing logic
- Save to ChromaDB
- Retrieve text using a query

---

## Sample Semantic Query

```python
print(retrieve_from_chroma("modern version of chapter 1"))
```

---

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) with a downloaded model (e.g., llama3)
- Playwright
- ChromaDB

---

## Credits

- Text source: [Wikisource](https://en.wikisource.org)
- AI models: Local LLMs via [Ollama](https://ollama.com)
- Vector DB: [ChromaDB](https://www.trychroma.com)
