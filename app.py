import streamlit as st
from chunking import load_documents, chunk_text

st.markdown(
    "<h1 style='text-align: center;'>Financial Research Copilot</h1>",
    unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;' >AI-Powered Financial Analysis Assistant</p>",
    unsafe_allow_html=True)


user_query = st.text_input(
    "",
    placeholder="Ask for financial advise...")

if user_query:
    st.write("Analyzing..")

"""Loading an chunking the .txt files"""
docs = load_documents()
all_chunks = []

for doc in docs:
    chunks = chunk_text(doc["text"])

    for chunk in chunks:
        all_chunks.append({"source": doc["source"], "text": chunk})
