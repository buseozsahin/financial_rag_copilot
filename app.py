import streamlit as st
from retrieval import search
from llm import get_llm_answer
st.markdown(
    "<h1 style='text-align: center;'>Financial Research Copilot</h1>",
    unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;' >AI-Powered Financial Analysis Assistant</p>",
    unsafe_allow_html=True)

user_query = st.text_input(
    "",
    placeholder="Ask for financial advise...")

if user_query:
    results = search(user_query)
    chunks = [r["text"] for r in results]

    answer = get_llm_answer(user_query, chunks)

    generated_ans = answer
    st.write(answer)