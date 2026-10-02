# 🌾 AgroRAG

AI-powered Agriculture Advisory System using Retrieval-Augmented Generation (RAG).

AgroRAG is a Streamlit-based application that provides agriculture-related answers using general AI knowledge or information retrieved from uploaded agriculture PDF documents.

## 🚀 Live Demo

[Open AgroRAG Live Demo](https://agrorag-grzdftdgbasqktyhqpf2sb.streamlit.app/)

## 📸 Screenshots

![AgroRAG - PDF Mode](screenshot.png)

![AgroRAG - General Mode](screenshot-general.png)

## 🚀 Features

- 📄 Upload agriculture PDF documents
- 🔍 Extract and split document text into chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗂️ Store and search embeddings using FAISS
- 🔎 Retrieve relevant information from uploaded documents
- 🤖 Generate answers using a Groq-hosted LLM
- 🌱 Agriculture-focused question answering
- 💬 General knowledge mode without a PDF
- 🔄 RAG mode when a PDF is uploaded
- 🌐 Deployed on Streamlit Cloud

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- Groq API
- GPT-OSS 20B
- PyPDF
- NumPy

## 🔄 Architecture

### 📄 RAG Mode – With PDF

PDF  
↓  
Text Extraction  
↓  
Text Chunking  
↓  
Sentence Transformer Embeddings  
↓  
FAISS Vector Search  
↓  
Relevant Context Retrieval  
↓  
Groq LLM  
↓  
Agriculture Answer

### 🤖 General Knowledge Mode – Without PDF

User Question  
↓  
Groq LLM  
↓  
Agriculture Answer

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Pavan10328/AgroRAG.git
cd AgroRAG

python -m venv venv

venv\Scripts\activate

.streamlit/secrets.toml

GROQ_API_KEY = "your_groq_api_key"

python -m streamlit run app.py

python -m streamlit run app.py

💡 How It Works
Without PDF
The user enters an agriculture-related question.
The question is sent to the Groq-hosted LLM.
The LLM generates an agriculture-focused response.
The generated answer is displayed in the Streamlit application.
With PDF
The user uploads an agriculture PDF.
PDF text is extracted using PyPDF.
The extracted text is divided into smaller chunks.
Sentence Transformers generate embeddings for the text chunks.
FAISS stores the embeddings for similarity search.
The user's question is converted into an embedding.
FAISS retrieves the most relevant document chunks.
The retrieved context is passed to the Groq-hosted LLM.
The LLM generates an answer using the retrieved context.
The answer is displayed in the Streamlit application.
🔍 RAG Pipeline
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Context + Question
      ↓
GPT-OSS 20B via Groq
      ↓
Generated Agriculture Answer
📁 Project Structure
AgroRAG/
│
├── data/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── requirements.txt
├── READ.md
└── .gitignore
🔐 Security
API keys are stored using Streamlit secrets.
The .streamlit/secrets.toml file is excluded from Git.
API credentials should never be committed to the GitHub repository.
🌐 Deployment

The application is deployed using Streamlit Cloud.

Live Application

Open AgroRAG Live Demo

Source Code

View AgroRAG on GitHub

🎯 Project Objective

The objective of AgroRAG is to demonstrate the practical use of Retrieval-Augmented Generation (RAG) for agriculture-related question answering by combining:

Document processing
Semantic embeddings
Vector similarity search
Context retrieval
Large Language Models
Streamlit-based application development

The project demonstrates how external documents can be combined with an LLM to generate context-aware responses.

👨‍💻 Author

Pavan Meesala

GitHub: Pavan10328

```bash
git clone https://github.com/Pavan10328/AgroRAG.git
cd AgroRAG
