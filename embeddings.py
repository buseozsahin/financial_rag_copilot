from sentence_transformers import SentenceTransformer
from chunking import build_chunks

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return model.encode(text)

def build_embeddings():
    all_chunks = build_chunks()
    chunks_with_vector = []

    for chunk in all_chunks:
        text = chunk["text"]

        embedding = get_embedding(text)
        chunks_with_vector.append({"source": chunk["source"], "text": text, "embedding": embedding})

    return chunks_with_vector