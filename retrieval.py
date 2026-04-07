from embeddings import model
from faiss_index import build_faiss
import numpy as np

def search(user_query, count_match_chunks = 3):
    index, chunks = build_faiss()

    query_vector = model.encode(user_query)
    query_vector = np.array([query_vector]).astype("float32")
    distance, indices = index.search(query_vector, count_match_chunks)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results