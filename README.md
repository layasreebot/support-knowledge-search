# 🔍 Support Knowledge Search

**A Semantic Search System for Support Knowledge using Generative AI**

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://www.langchain.com/)
[![Git](https://img.shields.io/badge/Version%20Control-Git-orange.svg)](https://git-scm.com/)

## 📌 Project Overview

Support Knowledge Search is a Generative AI-focused application designed to help users find relevant information from support-related knowledge sources efficiently.

Traditional keyword-based search may fail when a user's query uses different words from the original document. Semantic search addresses this limitation by representing text as embeddings and retrieving content based on semantic similarity.

This project explores semantic search, document retrieval, and GenAI application development using Python-based technologies.

## 🎯 Problem Statement

Support information is often distributed across documents, FAQs, troubleshooting guides, and knowledge articles. Finding the right information manually can consume time and effort.

The goal of this project is to develop a search system that helps users discover relevant support information through natural-language queries and semantic retrieval.

## 🎯 Objectives

- Improve access to support-related knowledge.
- Retrieve information based on query meaning.
- Explore text embeddings and vector similarity search.
- Build an interactive interface for searching support information.
- Establish a foundation for future Retrieval-Augmented Generation (RAG) capabilities.

## ✨ Key Features

- **Semantic Search:** Retrieve relevant content based on the meaning of a query.
- **Document Retrieval:** Find useful information from an indexed knowledge collection.
- **Embedding-Based Search:** Represent text as vectors for similarity comparison.
- **Interactive Interface:** Provide a user-friendly way to enter queries and view results.
- **Extensible Architecture:** Allow future integration of additional knowledge sources and AI-powered question answering.

> Features depend on the functionality implemented in the current version of the project.

## 🏗️ System Workflow

1. **Knowledge Collection:** Gather support articles and other relevant documents.
2. **Text Preprocessing:** Clean and split document content into manageable chunks.
3. **Embedding Generation:** Convert text chunks into vector representations.
4. **Indexing:** Store vectors in a suitable search index or vector database.
5. **Query Input:** Receive a user's search question.
6. **Semantic Retrieval:** Identify relevant content using similarity search.
7. **Result Presentation:** Display the retrieved information to the user.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API development |
| LangChain | Language-model and retrieval workflows |
| Streamlit | Interactive web interface, if used by the current implementation |
| FAISS / Chroma | Vector search and storage options |
| Text Embeddings | Semantic representation of documents |
| Git & GitHub | Version control and project hosting |

Only the technologies actually configured in the repository should be considered part of the implemented stack.

## ⚙️ Prerequisites

Install the following before running the application:

- Python 3
- Git
- Visual Studio Code (recommended)
- Project dependencies listed in `requirements.txt`, if available

If the frontend uses Streamlit, install its dependencies in the same Python environment unless the project specifies otherwise.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/layasreebot/support-knowledge-search.git
cd support-knowledge-search
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

If `requirements.txt` exists in the repository root:

```powershell
python -m pip install -r requirements.txt
```

If dependencies are maintained separately for the backend and frontend, install them according to their respective configuration files.

### 4. Configure Environment Variables

If the application requires API keys or other environment variables:

1. Check whether an `.env.example` file exists.
2. Create a local `.env` file using the documented configuration.
3. Add the required values.
4. Never commit API keys, passwords, or secrets to GitHub.

## ▶️ Running the Application

The following are common development commands. Check the actual entry-point filenames in your repository before running them.

### Backend — FastAPI

Open a terminal at the project root, activate the virtual environment, and run the command matching your backend entry point.

If the entry point is `backend/main.py` and it exposes an object named `app`:

```powershell
python -m uvicorn backend.main:app --reload
```

If the backend uses a different module path, update the command accordingly.

After the server starts, open:

- API root: `http://127.0.0.1:8000/`
- Interactive API documentation: `http://127.0.0.1:8000/docs`

### Frontend — Streamlit

Open a second terminal and activate the required virtual environment.

If the frontend entry point is `frontend/app.py`:

```powershell
python -m streamlit run frontend/app.py
```

If the project uses a different Streamlit entry point, replace the path with the correct filename.

The terminal will display the local URL for the interface, commonly `http://localhost:8501`.

### Verify the Application

1. Confirm that the backend starts without errors.
2. Open the FastAPI documentation page if FastAPI is configured.
3. Start the frontend in a separate terminal if required.
4. Enter a sample support-related query.
5. Check whether the application returns relevant search results.

## 📁 Project Structure

The structure below is illustrative. Adjust it to match the actual repository.

```text
support-knowledge-search/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   ├── app.py
│   └── ...
├── data/
│   └── ...
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔮 Future Enhancements

- Retrieval-Augmented Generation (RAG) for grounded answers.
- Support for PDF, DOCX, and other document formats.
- Improved semantic ranking and metadata filtering.
- Source references for retrieved information.
- Retrieval evaluation using suitable quality metrics.
- Automated testing and deployment.
- Integration with additional support knowledge sources.

## 🧪 Testing

Run the project's existing tests if a test suite is available.

For a FastAPI application, the interactive API documentation at `/docs` can help verify available endpoints.

Automated test commands should follow the project's configured test framework.

## 🔐 Security

- Store secrets in environment variables.
- Keep `.env` files out of version control.
- Do not upload confidential support documents or private user data.
- Validate inputs and handle errors appropriately.

## 👩‍💻 Author

**Layasree**  
B.Tech — Information Technology

## 📄 License

No license has been specified here. Add a suitable license file if you intend to distribute the project for reuse.

---

*Support Knowledge Search — exploring semantic search and Generative AI for more effective knowledge retrieval.*
