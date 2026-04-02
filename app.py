import os
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

# if user_query:
#     st.write("Answer:")
#ok     st.write("This is a simulated financial analysis based on your query.")


all_documents = []

for file_name in os.listdir("data"):
    with open(f"{"data"}/{file_name}", "r") as f:
        text = f.read()

        all_documents.append({
            "source": file_name,
            "text": text
        })
print(all_documents)
