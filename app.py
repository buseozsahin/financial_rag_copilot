import streamlit as st
from retrieval import search
from llm import get_llm_answer
from rag_config import get_rag_config
import time

st.markdown(
    "<h1 style='text-align: center;'>Financial Research Copilot</h1>",
    unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;' >AI-Powered Financial Analysis Assistant</p>",
    unsafe_allow_html=True)

user_query = st.text_input("", placeholder="Ask for financial advise...")


mode = st.radio("Response Mode:", ["fast", "balanced", "accurate"])

if user_query:
    start_time = time.time()

    config = get_rag_config(mode)

    with st.spinner():
        results = search(user_query, mode)
        chunks = [r["text"] for r in results]
        result = get_llm_answer(user_query, chunks, mode)

    end_time = time.time()
    duration = end_time - start_time

    answer = result["response"]
    prompt_tokens = result.get("prompt_eval_count")
    generated_tokens = result.get("eval_count")

    st.subheader("Answer")
    st.write(answer)

    st.divider()
    st.markdown(f"""
    **Time taken:** {duration:.2f} seconds  
    **Tokens spent:** {generated_tokens}  
    """)