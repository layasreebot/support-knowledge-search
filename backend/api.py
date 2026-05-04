import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from pydantic import BaseModel
from backend.search import search

app = FastAPI(title="Support Knowledge Search API")

class SearchRequest(BaseModel):
    query: str
    top_k: int = 3

@app.get("/")
def root():
    return {"message": "Support Search API is running!"}

@app.post("/search")
def search_endpoint(request: SearchRequest):
    results = search(request.query, request.top_k)
    return {"query": request.query, "results": results}