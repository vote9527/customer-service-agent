from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore
from rag.retriever import get_retriever


def build_retriever():

    docs = load_documents()

    chunks = split_documents(docs)

    embedding = get_embeddings()

    db = create_vectorstore(
        chunks,
        embedding
    )

    retriever = get_retriever(db)

    return retriever