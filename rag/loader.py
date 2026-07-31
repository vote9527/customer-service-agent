from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader


DOCUMENTS_DIR = Path(__file__).parent / "documents"


def load_documents():
    """
    加载企业知识库中的 Markdown 文档
    """

    loader = DirectoryLoader(
        str(DOCUMENTS_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8"
        }
    )

    documents = loader.load()

    print(f"成功加载 {len(documents)} 个文档")

    return documents


if __name__ == "__main__":
    documents = load_documents()

    for doc in documents:
        print("=" * 50)
        print("来源：", doc.metadata.get("source"))
        print("内容：")
        print(doc.page_content[:200])