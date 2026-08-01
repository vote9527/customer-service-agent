from langchain_core.tools import tool
from rag.pipeline import build_retriever
from utils.logger import logger


_retriever = None


def get_retriever():

    global _retriever

    if _retriever is None:
        logger.info(
            "初始化RAG Retriever"
        )
        _retriever = build_retriever()

    return _retriever



@tool
def search_policy(query:str):

    """
    查询企业政策知识库
    """

    logger.info(
        "====== RAG TOOL 被调用 ======"
    )

    logger.info(
        f"查询内容:{query}"
    )


    retriever = get_retriever()


    docs = retriever.invoke(query)


    logger.info(
        f"检索数量:{len(docs)}"
    )


    for i,doc in enumerate(docs):

        logger.info(
            f"""
Chunk {i+1}
来源:{doc.metadata.get("source")}
内容:{doc.page_content}
"""
        )


    return "\n\n".join(
    [
        f"""
来源:
{doc.metadata.get('source')}

内容:
{doc.page_content}
"""
        for doc in docs
    ]
)