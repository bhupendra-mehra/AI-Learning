import logging

logger = logging.getLogger(__name__)

order_id = "ORD12345"
amount = 25999

logger.info(
    "Order %s processed with amount %s",
    order_id,
    amount
)