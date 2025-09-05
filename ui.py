import streamlit as st
import os
from ingestion import doc_ingestion, pdf_processing
from retrieval import retrieval_func
from agent import response_generator
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("pinecone_api")

st.set_page_config(page_title="RAG Agent", layout="wide")
st.title("📄 RAG Agent with PDFs + Pinecone + Gemini")

uploaded_files = st.file_uploader("Upload up to 5 PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    if len(uploaded_files) > 2:
        st.error("⚠️ Please upload no more than 2 PDFs.")
    else:
        embedder, index = doc_ingestion(PINECONE_API_KEY)
        for uploaded_file in uploaded_files:
            file_path = f"temp_{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            pdf_processing(file_path, embedder, index)
        st.success("✅ PDFs successfully ingested!")

query = st.text_input("Enter your question:")
if query:
    embedder, index = doc_ingestion(PINECONE_API_KEY)
    docs = retrieval_func(index, embedder, query, top_k=3)

    context = "\n\n".join(docs)
    # st.write("📚 **Retrieved context:**")
    # st.write(context)

    answer = response_generator(query, context)
    st.subheader("💡 Answer:")
    st.write(answer)
