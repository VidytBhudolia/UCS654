# TOPSIS Web (Streamlit)

A simple Streamlit web app to run TOPSIS on an uploaded CSV/XLSX, validate inputs, and email the result.

## Features
- Upload CSV/XLSX
- Enter weights and impacts
- Validations (counts, numeric columns, '+'/'-' impacts)
- Download result as CSV
- Optional email delivery via SMTP

## Run locally
```bash
cd "Topsis Web"
pip install -r requirements.txt topsis-vidyt-102303747
streamlit run streamlit_app.py
```

To enable email, set environment variables before starting Streamlit:
```bash
$env:SMTP_HOST="smtp.gmail.com"
$env:SMTP_PORT="587"
$env:SMTP_USER="you@example.com"
$env:SMTP_PASS="<app-password>"
$env:SMTP_FROM="you@example.com"
```

## Deployment options

### Streamlit Community Cloud (recommended for Streamlit apps)
1. Push this repo to GitHub (which you have)
2. Go to https://share.streamlit.io
3. Connect your repo, pick the branch and set `Topsis Web/streamlit_app.py` as the entry file
4. Add the SMTP env vars under app settings if you want email

### Vercel note
Vercel is optimized for static frontends + serverless functions. Streamlit runs a stateful server, which Vercel does not keep alive. If you must use Vercel, consider building a small FastAPI API + a static frontend instead of Streamlit. I can scaffold that if you want.
