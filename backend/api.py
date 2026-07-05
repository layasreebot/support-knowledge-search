import sys
import os
import csv
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Support Knowledge Search API")

LOG_FILE = "logs/query_log.csv"

def log_query(query, answer, sources, fallback):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            query,
            answer[:200],
            ", ".join([s["file_name"] for s in sources]),
            "Yes" if fallback else "No"
        ])

class SearchRequest(BaseModel):
    query: str
    top_k: int = 3

@app.get("/")
def root():
    return {"message": "Support Search API is running!"}

@app.post("/search")
def search_endpoint(request: SearchRequest):
    from backend.search import search
    result = search(request.query, request.top_k)
    log_query(
        request.query,
        result["answer"],
        result["citations"],
        result["fallback"]
    )
    return {
        "query": request.query,
        "answer": result["answer"],
        "citations": result["citations"],
        "fallback": result["fallback"]
    }

@app.post("/refresh")
def refresh_endpoint():
    try:
        from backend.ingest import ingest_documents
        ingest_documents()
        return {"status": "success", "message": "Knowledge base refreshed successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/logs")
def get_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 5:
                    logs.append({
                        "timestamp": row[0],
                        "query": row[1],
                        "answer": row[2],
                        "sources": row[3],
                        "fallback": row[4]
                    })
    return {"logs": list(reversed(logs))}