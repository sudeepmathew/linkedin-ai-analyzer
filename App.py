import streamlit as st
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    st.error("API key missing in .env")
    st.stop()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI LinkedIn Profile Analyzer")

uploaded_file = st.file_uploader(
    "Upload LinkedIn PDF",
    type=["pdf"]
)

def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


if uploaded_file:
    profile_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Profile Preview")
    st.write(profile_text[:2000])

    if st.button("Analyze Profile"):
        with st.spinner("Analyzing..."):

            prompt=f"""
Act as a LinkedIn profile coach.

Analyze this profile.

Provide:
1. Profile score out of 100
2. Headline suggestions
3. About section improvements
4. Experience bullet improvements

Profile:
{profile_text[:12000]}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )

            st.subheader("Analysis")
            st.write(
                response.choices[0].message.content
            )