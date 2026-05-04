import streamlit as st
import requests

st.set_page_config(
    page_title="Support Knowledge Search",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Support Knowledge Search")
st.markdown("Search support articles, tickets, and SOPs using AI")
st.divider()

col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_input(
        "💬 Ask your question:",
        placeholder="e.g. How do I reset my password?"
    )

with col2:
    top_k = st.slider("Number of results", 1, 5, 3)

if st.button("🔍 Search", use_container_width=True) and query:
    with st.spinner("Searching knowledge base..."):
        try:
            response = requests.post(
                "http://localhost:8000/search",
                json={"query": query, "top_k": top_k}
            )
            results = response.json().get("results", [])
        except:
            st.error("❌ Could not connect to API. Make sure the backend is running.")
            results = []

    if results:
        st.success(f"Found {len(results)} results for: **{query}**")
        st.divider()
        for r in results:
            with st.expander(f"📄 Result #{r['rank']} — {r['source']}"):
                st.markdown("**Content:**")
                st.info(r["content"])
                st.caption(f"📁 Source file: `{r['source']}`")
    else:
        st.warning("No results found. Try a different question.")

st.divider()
st.caption("Powered by HuggingFace Embeddings + FAISS + FastAPI")