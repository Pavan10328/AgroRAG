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
- Llama-based LLM
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
