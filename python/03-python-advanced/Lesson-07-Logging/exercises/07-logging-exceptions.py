import logging

logging.basicConfig(
    filename = "exception.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s - %(lineno)d"
)

try:
    number = 10
    restul = number / 0
except Exception:
    logging.exception("An error occurred")