import os
import logging


os.makedirs(
    "logs",
    exist_ok=True
)


logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s "
        "%(message)s"
    ),
    encoding="utf-8"
)


logger = logging.getLogger(
    "customer-agent"
)


logger.setLevel(
    logging.INFO
)


# 第三方库降噪

for name in [
    "httpx",
    "sentence_transformers",
    "transformers",
    "huggingface_hub",
    "urllib3"
]:

    logging.getLogger(
        name
    ).setLevel(
        logging.WARNING
    )