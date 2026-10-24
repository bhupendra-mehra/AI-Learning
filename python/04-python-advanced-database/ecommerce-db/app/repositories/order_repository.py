def create_order(
    connection, customer_id: int, order_number: str, status: str, total_amount: float
):

    cursor = None

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO orders
                (
                    customer_id,
                    order_number,
                    status,
                    total_amount
                )
            VALUES
                (%s, %s, %s, %s)
            """,
            (customer_id, order_number, status, total_amount),
        )

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()


def create_order_items(
    connection,
    order_id: int,
    product_id: int,
    quantity: int,
    price: float,
    subtotal: float,
):

    cursor = None

    try:

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO order_items
                (
                    order_id,
                    product_id,
                    quantity,
                    unit_price,
                    subtotal
                )
            VALUES
                (%s, %s, %s, %s, %s)
            """,
            (order_id, product_id, quantity, price, subtotal),
        )

        return cursor.lastrowid

    finally:

        if cursor:
            cursor.close()
