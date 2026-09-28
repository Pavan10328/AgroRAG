# 🌾 AgroRAG

AI-powered Agriculture Advisory System using Retrieval-Augmented Generation (RAG).
## 📸 Screenshots

![AgroRAG - PDF Mode](screenshot.png)
![AgroRAG - General Mode](screenshot-general.png)

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

## ⚙️ Setup

1. Clone the repository

```bash
git clone https://github.com/Pavan10328/AgroRAG.git
cd AgroRAG
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Install [Ollama](https://ollama.com) and pull the model

```bash
ollama pull llama3.2
```

## ▶️ Run the Project

```bash
python -m streamlit run app.py
```
