import faiss
from embeddings import build_embeddings
import numpy as np

chunks = build_embeddings()
def collect_all_embedded_text():
    vectors = []

    for chunk in chunks:
        vectors.append(chunk["embedding"])

    return vectors

def build_faiss():
    vectors = collect_all_embedded_text()

    vectors = np.array(vectors).astype("float32")
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    return index, chunks