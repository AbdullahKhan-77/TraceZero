# TraceZero

AI-powered personal data removal agent. Scans data broker websites for your personal information and automates opt-out / removal requests.

## What it does

- Scrapes live data broker sites (Intelius, Addresses.com, ZabaSearch) using Playwright
- Runs RoBERTa NER to detect PII (names, locations, phone numbers, emails)
- Runs DistilBERT to classify risk level (High / Medium / Low)
- Runs Sentence-BERT to score identity match confidence
- Automates opt-out form submissions via Playwright browser handlers
- Generates GDPR Art.17 / CCPA 1798.105 removal request emails
- Stores all records in SQLite via a FastAPI REST backend

## Stack

- **Backend:** FastAPI + Uvicorn
- **AI Models:** RoBERTa (NER), DistilBERT (risk classification), Sentence-BERT (identity match)
- **Scraping:** Playwright (real browser automation)
- **Database:** SQLite
- **Frontend:** Next.js 16 + React 19 — [TraceZero Frontend](https://github.com/AbdullahKhan-77/TraceZero-frontend)

## Project Structure

```
TraceZero/
├── main.py                  # FastAPI app — /scan, /enforce, /records endpoints
├── requirements.txt
├── ai_engine/
│   └── ner_pipeline.py      # RoBERTa NER, DistilBERT risk, Sentence-BERT match
├── scraper/
│   ├── scraper.py           # Playwright live scraper (3 brokers)
│   └── browser.py           # Opt-out form automation handlers
├── enforcement/
│   └── email_sender.py      # GDPR/CCPA removal email generator
|   └── form_filler.py       # automatically fills out opt-out form
├── database/
│   └── db.py                # SQLite init, insert, query, update
├── model_training/          # Training scripts for the AI models
└── dashboard/               # Streamlit dashboard
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/scan` | Scan brokers for a person's data |
| POST | `/enforce` | Send opt-out request for a record |
| GET | `/records` | Retrieve all stored scan records |

### Scan request body
```json
{
  "name": "John Smith",
  "city": "New York",
  "state": "NY",
  "phone": "5551234567",
  "email": "john@example.com"
}
```

## Setup

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run the API
python main.py
# Server starts at http://localhost:8000
```

## Author

Abdullah Khan
