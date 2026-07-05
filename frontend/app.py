import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="Support Knowledge Search",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1F4E79, #2E75B6);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .stat-box {
        background: #1F4E79;
        padding: 15px;
        border-radius: 8px;
        color: white;
        text-align: center;
    }
    .badge-article {
        background: #2E75B6;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 12px;
    }
    .badge-ticket {
        background: #E67E22;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 12px;
    }
    .badge-sop {
        background: #27AE60;
        color: white;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_logs" not in st.session_state:
    st.session_state.show_logs = False
if "total_searches" not in st.session_state:
    st.session_state.total_searches = 0
if "total_fallbacks" not in st.session_state:
    st.session_state.total_fallbacks = 0

# Header
st.markdown("""
<div class="main-header">
    <h1>🔍 Support Knowledge Search</h1>
    <p>AI-powered semantic search over support articles, tickets, and SOPs</p>
</div>
""", unsafe_allow_html=True)

# Stats Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🔍 Total Searches", st.session_state.total_searches)
with col2:
    st.metric("✅ Successful", st.session_state.total_searches - st.session_state.total_fallbacks)
with col3:
    st.metric("⚠️ Fallbacks", st.session_state.total_fallbacks)

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Panel")

    if not st.session_state.logged_in:
        st.markdown("### 🔐 Admin Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", use_container_width=True):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.is_admin = True
                st.session_state.logged_in = True
                st.success("✅ Logged in as Admin!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")
    else:
        st.success("✅ Logged in as Admin")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.is_admin = False
            st.session_state.logged_in = False
            st.rerun()

    st.divider()

    if st.session_state.is_admin:
        st.markdown("### 🛠️ Admin Controls")
        if st.button("🔄 Refresh Knowledge Base", use_container_width=True):
            with st.spinner("Refreshing..."):
                try:
                    response = requests.post("http://localhost:8000/refresh")
                    result = response.json()
                    if result["status"] == "success":
                        st.success("✅ " + result["message"])
                    else:
                        st.error("❌ " + result["message"])
                except:
                    st.error("❌ Could not connect to API.")

        if st.button("📊 View Query Logs", use_container_width=True):
            st.session_state.show_logs = not st.session_state.show_logs

        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.total_searches = 0
            st.session_state.total_fallbacks = 0
            st.success("✅ Cleared!")

    st.divider()
    st.markdown("### 💡 You can ask about:")
    st.markdown("- 🔑 Password reset")
    st.markdown("- 💳 Billing issues")
    st.markdown("- 🔒 Account locked")
    st.markdown("- 📋 Escalation process")
    st.divider()
    st.markdown("### 🛠️ Tech Stack")
    st.markdown("- 🤖 Groq LLaMA3")
    st.markdown("- 🧠 HuggingFace Embeddings")
    st.markdown("- 📦 FAISS Vector Store")
    st.markdown("- ⚡ FastAPI + Streamlit")

# Show logs
if st.session_state.is_admin and st.session_state.show_logs:
    st.markdown("### 📊 Query Logs")
    try:
        response = requests.get("http://localhost:8000/logs")
        logs = response.json().get("logs", [])
        if logs:
            for log in logs:
                with st.expander(f"🕐 {log['timestamp']} — {log['query']}"):
                    st.markdown(f"**Query:** {log['query']}")
                    st.markdown(f"**Answer:** {log['answer']}...")
                    st.markdown(f"**Sources:** `{log['sources']}`")
                    st.markdown(f"**Fallback:** `{log['fallback']}`")
        else:
            st.info("No logs yet.")
    except:
        st.error("❌ Could not fetch logs.")
    st.divider()

# Main Search Section
col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input(
        "💬 Ask your question:",
        placeholder="e.g. How do I reset my password?"
    )
with col2:
    top_k = st.slider("Number of sources", 1, 5, 3)

if st.button("🔍 Search", use_container_width=True) and query:
    with st.spinner("Searching and generating answer..."):
        try:
            response = requests.post(
                "http://localhost:8000/search",
                json={"query": query, "top_k": top_k}
            )
            data = response.json()
            answer = data.get("answer", "")
            citations = data.get("citations", [])
            fallback = data.get("fallback", False)
        except:
            st.error("❌ Could not connect to API. Make sure the backend is running.")
            answer = ""
            citations = []
            fallback = False

    if answer:
        st.session_state.total_searches += 1
        if fallback:
            st.session_state.total_fallbacks += 1
        st.session_state.chat_history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "query": query,
            "answer": answer,
            "citations": citations,
            "fallback": fallback
        })
        st.rerun()

# Display chat history
if st.session_state.chat_history:
    st.markdown("### 💬 Chat History")
    for chat in reversed(st.session_state.chat_history):
        with st.container():
            st.markdown(f"**🕐 {chat['time']} — ❓ {chat['query']}**")
            if chat["fallback"]:
                st.warning(chat["answer"])
                st.info("💡 Try asking about: password reset, billing issues, account access, or escalation procedures.")
            else:
                st.success(chat["answer"])
                if chat["citations"]:
                    with st.expander("📄 View Citations"):
                        for c in chat["citations"]:
                            badge = "badge-article"
                            if c["source_type"] == "Support Ticket":
                                badge = "badge-ticket"
                            elif c["source_type"] == "SOP Document":
                                badge = "badge-sop"
                            st.markdown(
                                f"**[{c['number']}] {c['file_name']}** "
                                f"<span class='{badge}'>{c['source_type']}</span>",
                                unsafe_allow_html=True
                            )
                            st.caption(f"📁 {c['source_path']} | ⭐ Score: {c['score']}")
                            st.info(c["excerpt"])
                            st.divider()
            st.divider()
else:
    st.info("💡 Ask a question above to get started!")

st.divider()
st.caption("🔍 Support Knowledge Search | Powered by Groq LLaMA3 + HuggingFace + FAISS + FastAPI")