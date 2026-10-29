# 🔍 Support Knowledge Search

A Generative AI-powered semantic search system that helps users find relevant information from support articles, tickets, and Standard Operating Procedures (SOPs).

## 📌 Project Overview

**Support Knowledge Search** is a semantic search application designed to improve the way users discover and retrieve support-related information. Instead of relying only on exact keyword matches, it uses text embeddings to understand the meaning of a user's query and retrieve relevant documents.

The project combines a FastAPI backend, LangChain for language-model application workflows, and Streamlit for an interactive user interface.

## 🎯 Objectives

- Enable meaning-based search across support documents.
- Reduce the time required to find relevant support information.
- Provide relevant results with highlighted matching content.
- Support filtering and source-document references.
- Build a foundation for a GenAI-powered support assistant.

## ✨ Key Features

- **Semantic Search:** Retrieve relevant content based on query meaning.
- **Embedding-Based Indexing:** Convert text into vector representations for similarity search.
- **Interactive Search UI:** Search and explore results through Streamlit.
- **Document Filtering:** Narrow results using available metadata.
- **Result Highlighting:** Make relevant text easier to identify.
- **Source References:** Help users trace results back to their original documents.
- **Question Answering:** Provide a foundation for answering questions using support knowledge.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API development |
| LangChain | LLM and retrieval workflows |
| Streamlit | Interactive web interface |
| FAISS / Chroma | Vector storage and similarity search |
| Text Embeddings | Semantic representation of documents |
| Git & GitHub | Version control and project hosting |

## ⚙️ How It Works

1. **Document Collection:** Collect support articles, tickets, and SOPs.
2. **Text Processing:** Extract and prepare document content for indexing.
3. **Embedding Generation:** Convert text chunks into vector embeddings.
4. **Vector Indexing:** Store embeddings in FAISS or Chroma.
5. **User Query:** Accept a question or search phrase through the interface.
6. **Semantic Retrieval:** Retrieve documents that are semantically relevant to the query.
7. **Result Display:** Display relevant content, highlights, and source references.

## 🚀 Getting Started

### Prerequisites

- Python installed on your system.
- Visual Studio Code (recommended).
- Git installed and configured.
- Required Python packages for the project.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If your repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

If your project uses an LLM provider or API keys, configure them using a `.env` file according to your project setup.

**Important:** Never commit API keys, passwords, or other secrets to GitHub.

### 5. Run the Application

The exact commands depend on your project structure.

For a typical FastAPI application:

```bash
uvicorn main:app --reload
```

For a typical Streamlit application:

```bash
streamlit run app.py
```

Replace `main:app` and `app.py` with the actual module and file names in your repository. Run the backend and frontend in separate terminals if your project uses separate applications.

## 📁 Suggested Project Structure

```text
support-knowledge-search/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   └── ...
├── data/
│   └── ...
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

This is an example structure; adapt it to your actual project files.

## 🔮 Future Enhancements

- Retrieval-Augmented Generation (RAG) for context-aware answers.
- Support for multiple document formats.
- Advanced metadata-based filtering.
- Search result ranking and reranking.
- Evaluation of retrieval quality and answer faithfulness.
- Conversation history and memory.
- Authentication and role-based access control.

## 🎓 Project Information

- **Project Name:** Support Knowledge Search
- **Category:** Semantic Search Systems
- **Domain:** Support
- **Focus Area:** Generative AI (GenAI)
- **Project Type:** AI-powered information retrieval system

## 👩‍💻 Author

**Layasree**

B.Tech – Information Technology

## 📄 License

This project is intended for educational and development purposes. Add a suitable open-source license if you plan to distribute the project publicly.
