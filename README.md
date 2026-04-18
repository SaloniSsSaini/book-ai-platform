# 📚 Book AI Platform (Backend) – RAG + Local LLM

## 🚀 Project Overview

This project is an AI-powered backend system for a Book Intelligence Platform built using **Retrieval-Augmented Generation (RAG)**.

It allows users to:

* Query books using natural language
* Retrieve relevant book data
* Generate intelligent answers using a Local LLM

---

## 🧠 Key Features

### 🔍 Hybrid Search

* Semantic search using embeddings
* Keyword-based retrieval
* Combined ranking for better accuracy

### 🤖 AI-Powered Q&A

* Uses RAG pipeline
* Context-aware responses
* Source-based answers

### 🧾 Chat Memory

* Stores previous queries and responses
* Enables future analytics

### 📊 Trending Queries

* Tracks most searched queries
* Useful for insights and recommendations

### ⚡ Fast Performance

* Embedding caching (Redis ready)
* Optimized retrieval pipeline

---

## 🏗️ System Architecture

User Query → Django API → RAG Pipeline → Vector DB → LLM → Response

---

## 🛠 Tech Stack

| Component        | Technology                     |
| ---------------- | ------------------------------ |
| Backend          | Django + Django REST Framework |
| Vector Database  | ChromaDB                       |
| Embeddings       | Sentence Transformers          |
| LLM              | LM Studio (Local API)          |
| Database         | SQLite                         |
| Cache (Optional) | Redis                          |

---

## 📁 Project Structure

```
backend/
│
├── apps/
│   ├── books/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │
│   ├── rag/
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── views.py
│
├── core/
│   └── llm.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone Repository

```
git clone https://github.com/SaloniSsSaini/book-ai-platform.git
cd book-ai-platform/backend
```

---

### 🔹 Step 2: Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 Step 4: Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 Step 5: Start Backend Server

```
python manage.py runserver
```

👉 Server runs at:

```
http://127.0.0.1:8000/
```

---

## 🤖 LLM Setup (VERY IMPORTANT)

This project uses a **local LLM via LM Studio**.

### Steps:

1. Open LM Studio
2. Download a model (Mistral / Llama)
3. Load the model
4. Click **Start Server**

👉 Ensure this is running:

```
http://localhost:1234
```

---

## 🔌 API Endpoints

### 📚 Get Books

```
GET /api/books/
```

Response:

```json
[
  {
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear"
  }
]
```

---

### 📖 Book Detail

```
GET /api/books/<id>/
```

---

### 🤖 Ask Question (RAG)

```
GET /api/ask/?q=your_question
```

Example:

```
/api/ask/?q=best productivity books
```

Response:

```json
{
  "answer": "Atomic Habits is one of the best productivity books...",
  "sources": ["Atomic Habits"]
}
```

---

## 🧪 Sample Queries

* What are the best books for productivity?
* Recommend books like Atomic Habits
* Suggest top fiction books
* Books for self improvement

---

## ⚠️ Common Issues & Fixes

### ❌ Error: `no such table`

✔ Run:

```
python manage.py migrate
```

---

### ❌ Error: `localhost:1234 refused`

✔ Start LM Studio server

---

### ❌ Large file push error

✔ Remove `venv` and use `.gitignore`

---

## 📌 Highlights

* Fully working RAG pipeline
* Local LLM integration (no API cost)
* Clean modular backend architecture
* Scalable design

---

## 📌 Future Improvements

* Streaming responses (typing effect)
* Multi-book comparison
* Advanced UI integration
* Cloud deployment

---

## 👩‍💻 Author

**Saloni Saini**

---

## ⭐ Final Note

This project demonstrates real-world implementation of:

* Generative AI
* RAG systems
* Full-stack AI integration

---

🚀 *Ready for production-level extension and deployment*
