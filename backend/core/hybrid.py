from rank_bm25 import BM25Okapi

def hybrid_search(query, docs):
    tokenized = [d.split() for d in docs]
    bm25 = BM25Okapi(tokenized)

    scores = bm25.get_scores(query.split())
    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    return [r[0] for r in ranked[:3]]