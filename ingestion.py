from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def doc_ingestion(pinecone_key, index_name="ragdocx"):
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    dim = embedder.get_sentence_embedding_dimension()

    pc = Pinecone(api_key=pinecone_key)

    # ✅ Check before creating
    existing_indexes = pc.list_indexes().names()
    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=dim,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")  
        )
        print(f"✅ Created new index: {index_name}")
    else:
        print(f"⚡ Index {index_name} already exists, skipping creation.")

    index = pc.Index(index_name)
    return embedder, index


def pdf_processing(file_path, embedder, index):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    for i, chunk in enumerate(chunks):
        text = chunk.page_content
        emb = embedder.encode(text).tolist()
        index.upsert([(f"{file_path}-{i}", emb, {"text": text})])

    print(f"[+] {file_path} ingested into Pinecone")
