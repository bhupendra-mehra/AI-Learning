from app.config.settings import Settings
from app.utils.helpers import format_currency
from app.models.order import Order
from app.services.order_service import process_order

def main() -> None:

    order = Order(
        order_id="ORD1001",
        customer="Bhupendra",
        amount=25000.0
    )


    process_order(order)

    print(order)



if __name__ == "__main__":
    main()
# settings = Settings()

# print(settings.api_key)

# print(format_currency(23343.99))
# print(format_currency(25999))