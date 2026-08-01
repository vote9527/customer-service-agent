import logging


logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    encoding="utf-8"
)


logger = logging.getLogger(
    "customer-agent"
)


logger.setLevel(
    logging.INFO
)


# 降低第三方库日志等级

logging.getLogger(
    "httpx"
).setLevel(logging.WARNING)


logging.getLogger(
    "sentence_transformers"
).setLevel(logging.WARNING)


logging.getLogger(
    "transformers"
).setLevel(logging.WARNING)