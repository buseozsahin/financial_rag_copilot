import os

"""Loading the dataset documents"""
def load_documents(folder = "data"):
    documents = []
    for file_name in os.listdir(folder):
        path = os.path.join(folder, file_name)

        with open(path, "r") as file:
            documents.append({"source": file_name, "text": file.read()})

    return documents

"""Chunking the loaded text"""
def chunk_text(text, chunk_size = 400, chunk_overlap = 80):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - chunk_overlap

    return chunks

"""Loading and chunking the .txt files"""
def build_chunks():
    docs = load_documents()
    all_chunks = []

    for doc in docs:
        chunks = chunk_text(doc["text"])

        for chunk in chunks:
            all_chunks.append({"source": doc["source"], "text": chunk})

    return all_chunks