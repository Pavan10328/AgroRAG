# 🌾 AgroRAG

AI-powered Agriculture Advisory System using Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

AgroRAG is an AI-based agriculture advisory application that provides answers to agriculture-related questions.

Users can upload agriculture-related PDF documents and ask questions. The system retrieves relevant information from the uploaded document and uses an LLM to generate a clear and useful answer.

## 🚀 Features

- 📄 Upload agriculture PDF documents
- ✂️ Split documents into smaller chunks
- 🔎 Generate semantic embeddings
- 🗂️ Store and search vectors using FAISS
- 🤖 Generate answers using Llama 3.2
- 🌱 Ask agriculture-related questions
- 💬 Supports general questions even without a PDF
- 🖥️ Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Llama 3.2
- Ollama
- PyPDF

## 🔄 How It Works

1. User uploads an agriculture PDF.
2. Text is extracted from the PDF.
3. The text is divided into chunks.
4. Sentence Transformers generates embeddings.
5. FAISS stores the embeddings for similarity search.
6. User asks a question.
7. Relevant document chunks are retrieved.
8. Llama 3.2 generates the final answer.

## 📂 Project Structure

```text
AgroRAG/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
