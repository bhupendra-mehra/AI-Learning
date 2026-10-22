import logging


orders = [
    ("ORD1001", 2500),
    ("ORD1002", 0),
    ("ORD1003", 1500),
]


logging.basicConfig(
    filename="order_processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)


def process_order(order_id, amount):

    try:
        logger.info(
            "Processing order %s",
            order_id
        )

        if amount <= 0:
            logger.warning(
                "Invalid amount for order %s: %f",
                order_id,
                amount
            )
        else:
            logger.info(
                "Order %s processed successfully",
                order_id
            )

    except Exception:
        logger.exception(
            "Failed to process order %s",
            order_id
        )


for order_id, amount in orders:
    process_order(order_id, amount)