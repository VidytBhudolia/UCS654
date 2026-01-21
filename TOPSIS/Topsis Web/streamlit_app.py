import os
import io
import re
from typing import List

import numpy as np
import pandas as pd
import streamlit as st

# Use the published PyPI package
from topsis_package.core import topsis  # type: ignore

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def parse_weights_impacts(weights_str: str, impacts_str: str) -> tuple[List[float], List[str]]:
    weights = [float(w.strip()) for w in weights_str.split(",") if w.strip() != ""]
    impacts = [i.strip() for i in impacts_str.split(",") if i.strip() != ""]
    if any(i not in {"+", "-"} for i in impacts):
        raise ValueError("Impacts must be either '+' or '-' and separated by commas")
    return weights, impacts


def validate_dataframe(df: pd.DataFrame, weights: List[float], impacts: List[str]) -> None:
    if df.shape[1] < 3:
        raise ValueError("Input file must contain at least three columns (id + >=2 criteria)")
    # Ensure criteria columns are numeric
    crit = df.columns[1:]
    for c in crit:
        if not pd.api.types.is_numeric_dtype(df[c]):
            raise ValueError("From 2nd to last columns must be numeric only")
    if len(weights) != len(impacts) or len(weights) != len(crit):
        raise ValueError("Number of weights, impacts and criteria columns must be the same")


def run_topsis(df: pd.DataFrame, weights: List[float], impacts: List[str]) -> pd.DataFrame:
    ids = df.iloc[:, 0].astype(str).tolist()
    matrix = df.iloc[:, 1:].to_numpy(dtype=float)
    result = topsis(matrix, weights, impacts)
    out = df.copy()
    out["Topsis Score"] = result.scores
    out["Rank"] = result.ranks
    return out


def send_email_with_attachment(to_email: str, csv_bytes: bytes, filename: str = "output.csv") -> None:
    import smtplib
    from email.message import EmailMessage

    host = os.environ.get("SMTP_HOST")
    port = int(os.environ.get("SMTP_PORT", "587"))
    user = os.environ.get("SMTP_USER")
    pwd = os.environ.get("SMTP_PASS")
    sender = os.environ.get("SMTP_FROM", user)

    if not (host and user and pwd and sender):
        raise RuntimeError("SMTP credentials not configured (SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, SMTP_FROM)")

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender
    msg["To"] = to_email
    msg.set_content("Please find the TOPSIS result attached.")
    msg.add_attachment(csv_bytes, maintype="text", subtype="csv", filename=filename)

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, pwd)
        server.send_message(msg)


st.set_page_config(page_title="TOPSIS Web", page_icon="📊")
st.title("TOPSIS Web Service")

st.markdown("Upload an input file (CSV/XLSX), enter weights and impacts, optionally add an email to receive the result.")

uploaded = st.file_uploader("Input File", type=["csv", "xlsx"])
weights_str = st.text_input("Weights (comma-separated)", value="0.2,0.2,0.2,0.2,0.2")
impacts_str = st.text_input("Impacts (comma-separated '+'/'-')", value="+,+,+,+,+")
email = st.text_input("Email (optional)")

submit = st.button("Submit")

if submit:
    if uploaded is None:
        st.error("Please upload a CSV or XLSX file")
    else:
        try:
            if uploaded.name.lower().endswith(".xlsx"):
                df = pd.read_excel(uploaded)
            else:
                df = pd.read_csv(uploaded)

            weights, impacts = parse_weights_impacts(weights_str, impacts_str)
            validate_dataframe(df, weights, impacts)

            out_df = run_topsis(df, weights, impacts)
            st.success("TOPSIS computed successfully.")
            st.dataframe(out_df)

            csv_buf = io.StringIO()
            out_df.to_csv(csv_buf, index=False)
            csv_bytes = csv_buf.getvalue().encode("utf-8")
            st.download_button("Download CSV", data=csv_bytes, file_name="output.csv", mime="text/csv")

            if email:
                if not EMAIL_RE.match(email):
                    st.error("Please enter a valid email address")
                else:
                    try:
                        send_email_with_attachment(email, csv_bytes)
                        st.info("Result emailed successfully.")
                    except Exception as e:
                        st.warning(f"Could not send email: {e}")
        except Exception as e:
            st.error(str(e))
