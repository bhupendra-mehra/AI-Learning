import logging
from collections  import defaultdict
from app.models.order import Order


logger = logging.getLogger(__name__)

def process_order(order : Order) -> bool:


    try:
        
        logger.info(
            "Processing order %s",
            order.order_id
        )

        if order.amount <= 0 :
            logger.warning(
                "Invalid amount for order %s",
                order.order_id
            )

            return False

        order.status = "processed"

        logger.info(
            "Order %s successfully processed",
            order.order_id
        )

        return True

    except Exception:
        logger.execption(
            "Failed to process order %s",
            order.order_id
        )

        return False

def group_by_category(
    orders : list[Order]
) -> dict[str,list[Order]]:

    grouped = defaultdict(list)

    for order in orders :
        grouped[order.category].append(order)

    return dict(grouped)