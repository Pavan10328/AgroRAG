# 🌾 AgroRAG

AI-powered Agriculture Advisory System using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- 📄 Upload agriculture PDF documents
- 🔍 Extract and split document text
- 🧠 Generate semantic embeddings
- 🗂️ FAISS vector database for similarity search
- 🤖 Llama 3.2 local LLM using Ollama
- 🌱 Agriculture question answering
- 💬 Works with or without PDF documents

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- Ollama
- Llama 3.2
- PyPDF

## 🔄 Architecture

PDF → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → Llama 3.2 → Answer

Without PDF:

Question → Llama 3.2 → Answer

## ▶️ Run the Project

```bash
python -m streamlit run app.py  
