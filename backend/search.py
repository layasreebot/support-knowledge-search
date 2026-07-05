import os
import sys
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

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

def get_source_type(source_path):
    if "articles" in source_path:
        return "Support Article"
    elif "tickets" in source_path:
        return "Support Ticket"
    elif "sops" in source_path:
        return "SOP Document"
    else:
        return "Document"

def get_file_name(source_path):
    return os.path.basename(source_path)

def search(query, top_k=3):
    vector_store = load_vector_store()
    results = vector_store.similarity_search_with_score(query, k=top_k)

    context_parts = []
    citations = []

    for i, (doc, score) in enumerate(results):
        source_path = doc.metadata.get("source", "Unknown")
        file_name = get_file_name(source_path)
        source_type = get_source_type(source_path)

        context_parts.append(f"[{i+1}] {doc.page_content}")
        citations.append({
            "number": i + 1,
            "file_name": file_name,
            "source_type": source_type,
            "source_path": source_path,
            "excerpt": doc.page_content[:200],
            "score": round(float(score), 4)
        })

    context = "\n\n".join(context_parts)

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a helpful support assistant.
Use the following numbered support documents to answer the question.
Reference documents using [1], [2], [3] in your answer.
If the answer is not in the documents, say "I don't have enough information to answer this."

Support Documents:
{context}

Question: {question}

Answer:"""
    )

    chain = prompt | llm
    
    if context.strip():
        response = chain.invoke({"context": context, "question": query})
        answer = response.content
    else:
        answer = "I don't have enough information to answer this."

    fallback = False
    if "don't have enough information" in answer.lower() or not results:
        fallback = True

    return {
        "answer": answer,
        "citations": citations,
        "fallback": fallback
    }