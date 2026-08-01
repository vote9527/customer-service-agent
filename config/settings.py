import os
from dotenv import load_dotenv


load_dotenv()


DASHSCOPE_API_KEY = os.getenv(
    "DASHSCOPE_API_KEY"
)


MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "qwen-plus"
)


BASE_URL = os.getenv(
    "BASE_URL",
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        0.7
    )
)


RAG_TOP_K = int(
    os.getenv(
        "RAG_TOP_K",
        1
    )
)

