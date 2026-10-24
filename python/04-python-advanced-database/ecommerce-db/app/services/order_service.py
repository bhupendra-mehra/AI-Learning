from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product


class OrderService:
    def __init__(self, session: Session):
        self.session = session

    def create_order(self, customer_id: int, cart: dict) -> Order:
        if not cart:
            raise ValueError("Your shopping cart is empty.")

        order_items = []
        total_amount = Decimal("0.00")

        # Lock product rows while validating and creating the order.
        # This helps prevent concurrent checkouts overselling stock.
        for product_id, quantity in cart.items():
            try:
                product_id = int(product_id)
                quantity = int(quantity)
            except (TypeError, ValueError):
                raise ValueError("Your cart contains invalid items.")

            if quantity < 1:
                raise ValueError("Product quantities must be at least 1.")

            statement = (
                select(Product).where(Product.id == product_id).with_for_update()
            )
            product = self.session.scalar(statement)

            if product is None:
                raise ValueError(f"Product #{product_id} is no longer available.")

            if quantity > product.quantity:
                raise ValueError(
                    f"Insufficient stock for {product.name}. "
                    f"Available: {product.quantity}."
                )

            unit_price = Decimal(str(product.price))
            subtotal = unit_price * quantity
            total_amount += subtotal

            order_items.append(
                {
                    "product": product,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "subtotal": subtotal,
                }
            )

        order = Order(
            customer_id=customer_id,
            status="pending",
            total_amount=total_amount,
        )

        self.session.add(order)
        self.session.flush()

        for item in order_items:
            product = item["product"]

            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item["quantity"],
                unit_price=item["unit_price"],
                subtotal=item["subtotal"],
            )

            self.session.add(order_item)
            product.quantity -= item["quantity"]

        self.session.flush()
        return order
