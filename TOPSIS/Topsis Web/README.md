# TOPSIS Web (Streamlit)

Minimal Streamlit UI for TOPSIS: upload CSV/XLSX, enter weights/impacts, get ranked output, and send via email (SMTP).

## Live Demo
https://topsis-vidyt.streamlit.app/

## Run locally
```bash
cd "Topsis Web"
pip install streamlit pandas numpy openpyxl topsis-vidyt-102303747
streamlit run streamlit_app.py
```

## Email (SMTP)
Add secrets (Streamlit Cloud) or `.streamlit/secrets.toml` locally:
```toml
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"
SMTP_PASS = "xxxx xxxx xxxx xxxx"  # Gmail App Password
SMTP_FROM = "your_email@gmail.com"
```

## Deploy on Streamlit Cloud
1) Repo: `UCS654`, branch: `main`
2) Main file: `TOPSIS/Topsis Web/streamlit_app.py`
3) Add the SMTP secrets above in Settings → Secrets
4) Deploy
