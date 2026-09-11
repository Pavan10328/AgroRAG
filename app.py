import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
import faiss
import numpy as np

st.set_page_config(
    page_title="AgroRAG",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgroRAG")
st.subheader("AI-powered Agriculture Advisory System")

llm = ChatOllama(model="llama3.2")

uploaded_file = st.file_uploader(
    "📄 Upload an agriculture PDF",
    type=["pdf"]
)

question = st.text_input(
    "🌱 Ask your agriculture question"
)

# Initialize variables
chunks = []
model = None
index = None

# PDF Processing
if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    st.success("✅ PDF processed successfully!")
    st.write("📊 Total chunks:", len(chunks))

    if chunks:

        model = SentenceTransformer("all-MiniLM-L6-v2")

        embeddings = model.encode(chunks)

        embeddings = np.array(embeddings).astype("float32")

        index = faiss.IndexFlatL2(embeddings.shape[1])

        index.add(embeddings)

        st.success("✅ FAISS vector database created!")
        st.write("🔢 Vector count:", index.ntotal)

        with st.expander("📖 View first chunk"):
            st.write(chunks[0])

# Question Processing
if question:

    # If PDF is uploaded → Use RAG
    if uploaded_file and chunks and model and index:

        question_embedding = model.encode([question])

        question_embedding = np.array(
            question_embedding
        ).astype("float32")

        distances, indices = index.search(
            question_embedding,
            k=2
        )

        context = "\n\n".join(
            chunks[i] for i in indices[0]
        )

        prompt = f"""
You are an agriculture advisory assistant.

Answer the user's question using the information provided in the context.

Context:
{context}

Question:
{question}

Give a clear, simple and useful answer.
"""

    # If PDF is NOT uploaded → General LLM answer
    else:

        prompt = f"""
You are an agriculture advisory assistant.

Answer the user's agriculture-related question using your general knowledge.

Question:
{question}

Give a clear, simple and useful answer.
"""

    response = llm.invoke(prompt)

    st.subheader("🤖 AgroRAG Answer")

    st.write(response.content)