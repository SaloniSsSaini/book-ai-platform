import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("books")

def add_doc(id, text, emb):
    collection.add(ids=[str(id)], documents=[text], embeddings=[emb])

def search(emb):
    return collection.query(query_embeddings=[emb], n_results=3)