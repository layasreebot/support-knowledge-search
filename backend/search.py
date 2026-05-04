import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    vector_store = FAISS.load_local(
        "vector_store",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store

def search(query, top_k=3):
    vector_store = load_vector_store()
    results = vector_store.similarity_search(query, k=top_k)
    output = []
    for i, doc in enumerate(results):
        item = {
            "rank": i + 1,
            "content": doc.page_content,
            "source": doc.metadata.get("source", "Unknown")
        }
        output.append(item)
    return output

if __name__ == "__main__":
    print("Testing search...\n")
    results = search("how to reset password")
    for r in results:
        print("Rank:", r["rank"])
        print("Source:", r["source"])
        print("Content:", r["content"])
        print("---")