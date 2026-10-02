import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from groq import Groq
import faiss
import numpy as np


st.set_page_config(
    page_title="AgroRAG",
    page_icon="🌾",
    layout="wide"
)


st.title("🌾 AgroRAG")
st.subheader("AI-powered Agriculture Advisory System")


# -----------------------------
# Load Embedding Model
# -----------------------------

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


embedding_model = load_embedding_model()


# -----------------------------
# Groq LLM
# -----------------------------

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


# -----------------------------
# Session State
# -----------------------------

if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []


# -----------------------------
# PDF Upload
# -----------------------------

uploaded_file = st.file_uploader(
    "📄 Upload an agriculture PDF (Optional)",
    type=["pdf"]
)


# User PDF remove chesthe session clear avvadaaniki
if not uploaded_file:
    st.session_state.faiss_index = None
    st.session_state.chunks = []

    st.info(
        "💡 General Knowledge Mode: No PDF is uploaded, "
        "so responses are generated using general agricultural knowledge."
    )


# -----------------------------
# PDF Processing
# -----------------------------

if uploaded_file and st.session_state.faiss_index is None:

    with st.spinner("Processing PDF..."):

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        if text.strip():

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )

            chunks = splitter.split_text(text)

            st.session_state.chunks = chunks

            embeddings = embedding_model.encode(chunks)

            embeddings = np.array(embeddings).astype("float32")

            index = faiss.IndexFlatL2(embeddings.shape[1])

            index.add(embeddings)

            st.session_state.faiss_index = index

            st.success("✅ PDF processed! RAG Mode Active.")


# -----------------------------
# User Question
# -----------------------------

question = st.text_input(
    "🌱 Ask your agriculture question"
)


if question:

    with st.spinner("Generating answer..."):

        # -----------------------------
        # OPTION 1: PDF → RAG
        # -----------------------------

        if (
            st.session_state.faiss_index is not None
            and st.session_state.chunks
        ):

            st.caption(
                "🔍 Mode: RAG (Answering based on uploaded PDF)"
            )

            question_embedding = embedding_model.encode(
                [question]
            )

            question_embedding = np.array(
                question_embedding
            ).astype("float32")

            distances, indices = st.session_state.faiss_index.search(
                question_embedding,
                k=2
            )

            context = "\n\n".join(
                st.session_state.chunks[i]
                for i in indices[0]
            )

            prompt = f"""
You are an agriculture advisory assistant.

Answer the user's question using the information provided
in the context.

Context:

{context}

Question:

{question}

Give a clear, simple and useful answer.
"""


        # -----------------------------
        # OPTION 2: No PDF → General LLM
        # -----------------------------

        else:

            st.caption(
                "🤖 Mode: General Knowledge (No PDF attached)"
            )

            prompt = f"""
You are an agriculture advisory assistant.

Answer the user's agriculture-related question using your
general knowledge.

Question:

{question}

Give a clear, simple and useful answer.
"""


        # -----------------------------
        # Groq LLM Response
        # -----------------------------

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )


        answer = response.choices[0].message.content


        # -----------------------------
        # Display Answer
        # -----------------------------

        st.subheader("🤖 AgroRAG Answer")

        st.write(answer)