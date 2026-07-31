from langchain_chroma import Chroma


PERSIST_DIRECTORY = "./rag/db"


def create_vectorstore(chunks, embeddings):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    return vectorstore


def load_vectorstore(embeddings):

    vectorstore = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    return vectorstore