from langchain_core.tools import tool
from rag.pipeline import build_retriever

retriever = build_retriever()

@tool
def search_policy(query:str):

    """
    查询企业政策知识库
    """

    print("\n====== RAG TOOL 被调用 ======")
    print("查询内容:", query)


    docs = retriever.invoke(query)


    print("检索数量:", len(docs))


    for i,doc in enumerate(docs):
        print(
            f"Chunk {i+1}:",
            doc.page_content[:100]
        )


    return "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )