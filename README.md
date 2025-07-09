# Angular PrimeNG RAG System

A Retrieval-Augmented Generation (RAG) system for answering Angular and PrimeNG migration/upgrade questions. Features a modern chat UI, Python/Flask backend, ChromaDB vector store, and OpenAI integration.

---

## Features
- **Modern Chat UI**: Beautiful, dark, flowing, and responsive chat interface.
- **Python/Flask Backend**: Handles queries, document ingestion, and OpenAI LLM calls.
- **ChromaDB Vector Store**: Fast, persistent semantic search over migration/upgrade docs.
- **OpenAI Embeddings**: Uses `text-embedding-ada-002` for chunk/document similarity.
- **PDF/Doc Ingestion**: Easily add new migration guides to `helper-files/`.

---

## Quickstart

### 1. Prerequisites
- Python 3.9+
- Node.js (for static asset development, optional)
- OpenAI API Key (get from https://platform.openai.com/)

### 2. Clone the Repo
```bash
git clone https://github.com/schauerjosh/angular-primeng-rag.git
cd angular-primeng-rag
```

### 3. Set Up Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

### 4. Ingest Documents
Put your migration/upgrade PDFs in `helper-files/`.
```bash
python src/main.py
```

### 5. Run the App
```bash
python src/app.py
```
Visit [http://localhost:5003](http://localhost:5003)

---

## Project Structure
```
.
├── src/                # Python backend
│   ├── app.py           # Flask app
│   ├── main.py          # Ingestion script
│   ├── ...
├── static/            # JS/CSS assets
├── templates/          # HTML templates
├── helper-files/       # Migration/upgrade PDFs
├── tests/              # Unit tests
├── requirements.txt    # Python dependencies
├── .gitignore
├── README.md
├── docs/               # Static UI for GitHub Pages
```

---

## Debugging & Development
- **Logs**: All major steps print debug info to the console.
- **ChromaDB**: Data is stored in `chroma_db/` (ignored by git).
- **API Key**: Never commit your OpenAI key. Use environment variables only.
- **Static UI**: Edit `static/styles.css` and `static/script.js` for UI tweaks.
- **Backend**: Edit `src/` Python files for logic changes.
- **Unit Tests**: Place tests in `tests/` and run with `pytest`.

---

## Deployment
### Flask App (Recommended)
- Deploy to [Render](https://render.com/), [Railway](https://railway.app/), or [Fly.io](https://fly.io/) for free hosting of Python/Flask apps.
- GitHub Pages **cannot** host Python/Flask backends (static only).

### Static UI (GitHub Pages)
- You can host the static UI (HTML/CSS/JS) on GitHub Pages, but backend features (search, LLM) will not work.
- To do this, copy `templates/index.html` and the `static/` folder to a `docs/` directory, commit, and enable Pages in repo settings.
- The provided `docs/index.html` and `docs/styles.css` are ready for Pages.

---

## Step-by-Step: GitHub Pages Static UI
1. Ensure `docs/index.html` and `docs/styles.css` exist (see this repo).
2. Commit and push to your repo.
3. In GitHub, go to **Settings > Pages** and set source to `docs/` folder.
4. Visit your Pages URL (see repo settings).

---

## Step-by-Step: Deploy Flask Backend (Render Example)
1. Fork this repo to your GitHub account.
2. Create a new web service on [Render](https://render.com/):
   - Connect your repo.
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python src/app.py`
   - Add environment variable: `OPENAI_API_KEY=sk-...`
3. Deploy and visit your Render URL.

---

## Contributing
PRs welcome! Please open issues for bugs or feature requests.

---

## License
MIT
