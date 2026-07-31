from rag.loader import load_documents
from rag.splitter import split_documents


docs = load_documents()


chunks = split_documents(docs)


print(
    "原文数量:",
    len(docs)
)


print(
    "切分后:",
    len(chunks)
)


for c in chunks[:3]:

    print("================")

    print(
        "长度:",
        len(c.page_content)
    )

    print(
        c.page_content[:100]
    )