# TOPSIS Web (Streamlit)

A simple Streamlit web app to run TOPSIS on an uploaded CSV/XLSX, validate inputs, download results, and email them.

## Features
- Upload CSV/XLSX (drag & drop or browse)
- Enter weights and impacts
- Comprehensive validations (counts, numeric columns, '+'/'-' impacts)
- View results in table format
- Download result as CSV
- Email delivery via SMTP

## Live Demo

🌐 https://topsis-vidyt.streamlit.app/

## Run locally
```bash
cd "Topsis Web"
pip install streamlit pandas numpy openpyxl topsis-vidyt-102303747
streamlit run streamlit_app.py
```

## Email Configuration

Email delivery works automatically when SMTP secrets are configured.

### For Streamlit Cloud:
1. Go to your app on https://share.streamlit.io
2. Click ⚙️ Settings → Secrets
3. Add the following (use your Gmail and App Password):
```toml
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"
SMTP_PASS = "xxxx xxxx xxxx xxxx"
SMTP_FROM = "your_email@gmail.com"
```
4. Save and restart the app

### For Local Development:
Create `.streamlit/secrets.toml` in the `Topsis Web` folder:
```toml
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"
SMTP_PASS = "xxxx xxxx xxxx xxxx"
SMTP_FROM = "your_email@gmail.com"
```

### Gmail App Password Setup:
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to https://myaccount.google.com/apppasswords
4. Generate new password for "Mail" or "Streamlit"
5. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)
6. Use it as `SMTP_PASS` in secrets

## Deploy on Streamlit Cloud

1. Push repo to GitHub
2. Go to https://share.streamlit.io
3. Connect GitHub account
4. Select repository: `UCS654`, branch: `main`
5. Set main file: `TOPSIS/Topsis Web/streamlit_app.py`
6. Add SMTP secrets in Settings → Secrets
7. Deploy

## Deployment options

### Streamlit Community Cloud (Recommended)
Free hosting optimized for Streamlit apps with built-in secrets management.

Steps above cover full deployment process.
