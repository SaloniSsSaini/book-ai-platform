from core.embeddings import get_embedding
from core.vectorstore import search
from core.llm import query_llm

def answer_question(question):
    emb = get_embedding(question)
    results = search(emb)

    context = "\n".join(results['documents'][0])

    prompt = f"""
    Answer using context and cite sources:

    {context}

    Question: {question}
    """

    return {
        "answer": query_llm(prompt),
        "sources": results['documents'][0]
    }