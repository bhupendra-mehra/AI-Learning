import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_total(price, quantity):

    try:
        total = price * float(quantity)

        logger.info(
            "Calculated total: %s",
            total
        )

        return total

    except Exception:
        logger.exception(
            "Failed to calculate total"
        ) 
        return False


calculate_total(1000, 3)
calculate_total(1000, "invalid")