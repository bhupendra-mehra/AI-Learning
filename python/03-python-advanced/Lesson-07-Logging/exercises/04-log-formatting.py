import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(message)s - %(lineno)d"
)

logging = logging.getLogger("application")

logging.info("Application started")
logging.warning("Low inventory")