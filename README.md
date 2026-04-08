# Financial Rag Copilot

A user-controlled Retrieval-Augmented Generation (RAG) system that dynamically adjusts retrieval depth, response style, and LLM token usage based on selected modes: Fast, Balanced, and Accurate.

This project demonstrates a tradeoff between speed and accuracy in LLM-based systems.

## Features

Mode-based RAG system (Fast / Balanced / Accurate)
Dynamic chunk retrieval using FAISS
Embedding-based semantic search (SentenceTransformers)
Local LLM inference using Ollama (Llama 3.2)
User-controlled response speed vs accuracy
Token usage tracking (prompt + generated tokens)
Response time measurement
Interactive UI using Streamlit

## Installation

Clone the repository
Install Python dependency (requirements.txt)
```
pip install -r requirements.txt
```

Install Ollama llama3.2
```
curl -fsSL https://ollama.com/install.sh | sh
```
```
ollama pull llama3.2
```

## How to run?
Run the application
```
streamlit run app.py
```

## How it works?

1. Enter a question in the search bar like “Is investing in NVIDIA risky?”
2. Select a mode: 
  - Fast (gives a quick and short answer)
  - Balanced (gives medium detail)
  - Accurate (gives a more detailed response)
3. Based on the selected mode, the system retrieves relevant text chunks using FAISS and sends them to a local LLM (Ollama with Llama 3.2)
4. The LLM then generates a structured answer in Pros and Cons format and shows it along with response time and token usage

**Important Note**

This RAG system uses a small test dataset with only NVIDIA data. If you change the dataset and add other data, the system will still work and give answers based on the new data.
For best results, ask NVIDIA-related questions because the current data is only about NVIDIA.
