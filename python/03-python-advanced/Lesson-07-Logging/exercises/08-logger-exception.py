import logging

logger = logging.getLogger(__name__)

try:
    result = 10 / 0

except Exception:
    logger.exception("Failed to calculate result")