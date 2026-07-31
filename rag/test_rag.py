from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore


# 1. 加载原始文档
docs = load_documents()

# 2. 文档切分
chunks = split_documents(docs)

# 3. 加载 Embedding 模型
embedding = get_embeddings()

# 4. 创建向量数据库
db = create_vectorstore(
    chunks,
    embedding
)

# 5. 创建 Retriever
# 只返回最相似的 2 个 Chunk
retriever = db.as_retriever(
    search_kwargs={
        "k": 1
    }
)

# 6. 执行检索
docs = retriever.invoke(
    "退款需要什么条件？"
)

# 7. 查看实际检索数量
print("实际检索数量：", len(docs))

# 8. 打印检索结果
for i, doc in enumerate(docs, 1):
    print("=" * 50)
    print(f"Top {i}")
    print("来源：", doc.metadata.get("source"))
    print("内容长度：", len(doc.page_content))
    print("内容：")
    print(doc.page_content)