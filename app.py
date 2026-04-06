import streamlit as st

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
