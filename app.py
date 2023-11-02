import streamlit as st
from PyPDF2 import PdfReader
import openai

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    pdf_text = ""
    for page in pdf_reader.pages:  # Corrected the loop for extracting text from all pages
        pdf_text += page.extract_text()
    return pdf_text

st.title("PDF Question Answering App")

# Upload a PDF file
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file is not None:
    st.header("Ask a question about the PDF:")
    question = st.text_input("")

    if st.button("Get Answer"):
        pdf_text = extract_text_from_pdf(pdf_file)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Document: {pdf_text}\nQuestion: {question}\nAnswer:",
            max_tokens=50
        )
        answer = response.choices[0].text.strip()

        st.subheader("Answer:")
        st.write(answer)

st.sidebar.title("About")
st.sidebar.info(
    "This app allows you to upload a PDF file, ask questions about it, and get answers using OpenAI's GPT-3.5 Turbo model."
)
