from embeddings import model
from faiss_index import build_faiss
import numpy as np
from rag_config import get_rag_config

def search(user_query, mode):
    config = get_rag_config(mode)
    top_k = config["top_k"]
    
    index, chunks = build_faiss()

    query_vector = model.encode(user_query)
    query_vector = np.array([query_vector]).astype("float32")
    distance, indices = index.search(query_vector, top_k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results