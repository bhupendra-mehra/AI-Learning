import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug information")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Payment failed")
logging.critical("Database unavailable")