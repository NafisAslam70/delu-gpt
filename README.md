# DELU-GPT

A small Flask API and web interface for asking an AI assistant questions and generating learning support such as a weekly syllabus or task breakdown.

## API
- `POST /api/ask` — generate a response to a prompt
- `POST /api/syllabus` — create a weekly syllabus from subject, grade, and duration
- `POST /api/task-breakdown` — turn a task into smaller steps

## Tech
Python, Flask, Flask-CORS, and an Ollama-backed client.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

Configure the model service and connection details required by `utils/ollama_client.py`.
