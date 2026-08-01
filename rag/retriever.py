from config.settings import RAG_TOP_K
def get_retriever(vectorstore):

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k":RAG_TOP_K
        }
    )

    return retriever