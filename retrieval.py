def retrieval_func(index, embedder, query, top_k=3):
    query_emb = embedder.encode(query).tolist()
    results = index.query(vector=query_emb, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in results["matches"]]
