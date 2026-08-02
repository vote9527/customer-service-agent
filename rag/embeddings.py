from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import HF_TOKEN

def get_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name=
        "BAAI/bge-small-zh-v1.5",
        model_kwargs={
        "device":"cpu",
        "token":HF_TOKEN
        },
    )

    return embeddings