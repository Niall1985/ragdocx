# 📄 RAG Agent with PDFs + Pinecone + Gemini

This project implements a Retrieval-Augmented Generation (RAG) pipeline using **PDF ingestion**, **Pinecone vector database**, and **Google Gemini LLM**. Users can upload PDFs, query their contents, and receive AI-generated answers using context from the documents.

---

```
## 🗂 Project Structure

RAGDocx/
│── ingestion.py         # Handles PDF ingestion into Pinecone
│── retrieval.py         # Handles similarity search / retrieval
│── llm_helper.py        # Wraps Google Gemini LLM
│── agent.py             # Optional wrapper for LLM responses
│── ui.py                # Streamlit frontend
│── requirements.txt     # Python dependencies
│── .env                 # API keys

```

---

## ⚡ Features

- Upload multiple PDFs (up to 2 at a time)
- Automatic splitting of PDF text into chunks
- Embedding with `SentenceTransformer`
- Vector storage & retrieval using Pinecone
- Contextual answer generation using Google Gemini LLM
- Streamlit-based interactive UI

---

## 🛠 Setup Instructions

### 1. Clone the repository
```bash
git clone <repo_url>
cd ragdocx
````

### 2. Setup Python virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project root with the following:

```
PINECONE_API_KEY=your_pinecone_key
GOOGLE_API_KEY=your_google_gemini_key
```

---

## 📝 How to Use

### 1. Run the Streamlit App

```bash
streamlit run ui.py
```

### 2. Upload PDFs

* Upload up to 5 PDF files.
* PDFs will be automatically processed, split into chunks, embedded, and ingested into Pinecone.

### 3. Ask Questions

* Enter your query in the text input.
* Relevant context from your PDFs will be retrieved.
* Gemini LLM will generate an answer using the retrieved context.

---

## 🔹 File Descriptions

* **ingestion.py** – Loads PDFs, splits text into chunks, creates embeddings, and upserts them into Pinecone.
* **retrieval.py** – Queries Pinecone and returns top-K relevant chunks.
* **llm\_helper.py** – Wraps Google Gemini LLM for question-answering with context.
* **agent.py** – Optional wrapper for generating responses.
* **ui.py** – Streamlit interface for file upload and interactive QA.
* **requirements.txt** – Project dependencies.
* **.env** – Stores API keys securely.

---

## 📌 Dependencies

* Python 3.10+
* [Streamlit](https://streamlit.io/)
* [Pinecone](https://www.pinecone.io/)
* [Sentence-Transformers](https://www.sbert.net/)
* [LangChain](https://www.langchain.com/)
* Google Gemini API (`langchain-google-genai`)

---

## 🚀 Next Steps

* Expand to multiple file formats (DOCX, TXT, etc.)
* Add caching for faster query responses
* Enable batch ingestion and parallel processing
* Fine-tune LLM prompts for better answers

---

## ⚠️ Notes

* Ensure Pinecone free-tier usage stays within limits.
* Maximum of 2 PDFs per upload to avoid performance issues.
* Google Gemini API key required for LLM functionality.

---

