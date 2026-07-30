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
    "BASE_URL"
)