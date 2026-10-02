# 🌾 AgroRAG

AI-powered Agriculture Advisory System using Retrieval-Augmented Generation (RAG).

AgroRAG is a Streamlit application that answers agriculture-related questions using either general AI knowledge or information retrieved from uploaded agriculture PDF documents.

## 🚀 Live Demo

[Open AgroRAG Live Demo](https://agrorag-grzdftdgbasqktyhqpf2sb.streamlit.app/)

> Note: Free Streamlit apps go to sleep when inactive. If you see a "wake up" button, click it and wait 20-30 seconds.

## 📸 Screenshots

![AgroRAG - PDF Mode](screenshot.png)

![AgroRAG - General Mode](screenshot-general.png)

## ✨ Features

- 📄 Upload agriculture PDF documents
- 🔍 Extract and split document text into chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗂️ Store and search embeddings using FAISS
- 🔎 Retrieve relevant information from uploaded documents
- 🤖 Generate answers using a Groq-hosted LLM (GPT-OSS 20B)
- 💬 General knowledge mode when no PDF is uploaded
- 🔄 RAG mode when a PDF is uploaded
- 🌐 Deployed on Streamlit Cloud

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- Groq API (GPT-OSS 20B)
- PyPDF
- NumPy

## 🔄 Architecture

### RAG Mode (with PDF)

```
PDF → Text Extraction → Text Chunking → Sentence Transformer Embeddings
    → FAISS Vector Search → Relevant Context → Groq LLM → Answer
```

### General Knowledge Mode (without PDF)

```
User Question → Groq LLM → Answer
```

## 💡 How It Works

### Without PDF
1. The user enters an agriculture-related question.
2. The question is sent to the Groq-hosted LLM.
3. The generated answer is displayed in the app.

### With PDF
1. The user uploads an agriculture PDF.
2. Text is extracted using PyPDF.
3. The text is split into smaller chunks.
4. Sentence Transformers generate embeddings for the chunks.
5. FAISS stores the embeddings for similarity search.
6. The user's question is converted into an embedding.
7. FAISS retrieves the most relevant chunks.
8. The retrieved context and the question are sent to the Groq LLM.
9. The generated answer is displayed in the app.

## ⚙️ Setup (Run Locally)

### 1. Clone the repository

```bash
git clone https://github.com/Pavan10328/AgroRAG.git
cd AgroRAG
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a file `.streamlit/secrets.toml` and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

### 5. Run the app

```bash
python -m streamlit run app.py
```

## 📁 Project Structure

```
AgroRAG/
├── data/
├── app.py
├── requirements.txt
├── README.md
├── screenshot.png
├── screenshot-general.png
└── .gitignore
```

## 🔐 Security

- The API key is stored using Streamlit secrets.
- `.streamlit/secrets.toml` is listed in `.gitignore` and is not committed to GitHub.
- Never commit API keys to a public repository.

## 🌐 Deployment

Deployed on Streamlit Cloud. The Groq API key is added under **Settings → Secrets** in the Streamlit Cloud dashboard.

## 🎯 Project Objective

AgroRAG demonstrates how Retrieval-Augmented Generation can be used for agriculture question answering by combining document processing, semantic embeddings, vector similarity search, context retrieval, and a large language model in a Streamlit application.

## 👨‍💻 Author

**Pavan Meesala**
GitHub: [Pavan10328](https://github.com/Pavan10328)
