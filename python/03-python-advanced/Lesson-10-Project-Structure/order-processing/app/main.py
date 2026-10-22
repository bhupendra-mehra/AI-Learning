import logging

from app.models.order import Order
from app.services.order_service import (
    process_order,
    group_by_category
)
from app.utils.helpers import format_currency


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:

    orders: list[Order] = [

        Order(
            order_id="ORD1001",
            customer="Bhupendra Mehra",
            amount=60000.0,
            category="Electronics",
            quantity=2
        ),

        Order(
            order_id="ORD1002",
            customer="Rahul",
            amount=1500.0,
            category="Electronics",
            quantity=1
        ),

        Order(
            order_id="ORD1003",
            customer="Amit",
            amount=2500.0,
            category="Fashion",
            quantity=2
        )
    ]


    for order in orders:
        process_order(order)


    print("\nOrders:")

    for order in orders:

        print(
            order.order_id,
            order.customer,
            format_currency(order.total_price()),
            order.status
        )


    grouped = group_by_category(orders)

    print("\nGrouped by category:")

    for category, category_orders in grouped.items():

        print(
            category,
            "→",
            [order.order_id for order in category_orders]
        )


if __name__ == "__main__":
    main()