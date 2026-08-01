from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name=
        "BAAI/bge-small-zh-v1.5",
        model_kwargs={
        "device":"cpu"
        },
    )

    return embeddings