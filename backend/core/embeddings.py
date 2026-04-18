from sentence_transformers import SentenceTransformer
import redis, json

model = SentenceTransformer("all-MiniLM-L6-v2")
r = redis.Redis(host="localhost", port=6379)

def get_embedding(text):
    key = f"emb:{text}"

    if r.exists(key):
        return json.loads(r.get(key))

    emb = model.encode(text).tolist()
    r.set(key, json.dumps(emb))
    return emb