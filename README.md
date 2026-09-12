# WSL2 Ubuntu Dashboard

A small Flask dashboard that displays live system information, Ubuntu/WSL details, and a rotating programming quote.

## Features
- Ubuntu/WSL environment details
- Live clock and uptime display
- Random developer quote/joke API
- Tailwind-based dashboard UI

## Local setup

```bash
cd /home/ladmin/test-dashboard
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## Project structure

- `app.py` — Flask app and API routes
- `templates/index.html` — dashboard UI
- `requirements.txt` — Python dependencies
