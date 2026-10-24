from app.database.connection import get_connection
from app.models.product import Product
from app.repositories.product_repository import (
    create_product as repository_create_product,
)
from app.repositories.product_repository import (
    delete_product as repository_delete_product,
)
from app.repositories.product_repository import (
    get_product as repository_get_product,
)
from app.repositories.product_repository import (
    get_products as repository_get_products,
)
from app.repositories.product_repository import (
    update_product_price as repository_update_product_price,
)


def get_product(product_id: int) -> Product | None:

    connection = get_connection()

    try:

        row = repository_get_product(connection, product_id)

        if row is None:
            return None

        return Product(
            id=row["id"],
            category_id=row["category_id"],
            sku=row["sku"],
            name=row["name"],
            price=float(row["price"]),
            stock_quantity=int(row["stock_quantity"]),
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    finally:

        connection.close()


def create_product(
    category_id: int, sku: str, name: str, price: float, quantity: int
) -> int:

    connection = get_connection()

    try:

        product_id = repository_create_product(
            connection, category_id, sku, name, price, quantity
        )

        connection.commit()

        return product_id

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()


def update_product_price(product_id: int, price: float) -> int:

    connection = get_connection()

    try:

        affected_rows = repository_update_product_price(connection, product_id, price)

        connection.commit()

        return affected_rows

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()


def delete_product(product_id: int) -> int:

    connection = get_connection()

    try:

        affected_rows = repository_delete_product(connection, product_id)

        connection.commit()

        return affected_rows

    except Exception:

        connection.rollback()

        raise

    finally:

        connection.close()


def get_products() -> list[Product]:

    connection = get_connection()

    try:

        rows = repository_get_products(connection)

        return [
            Product(
                id=row["id"],
                category_id=row["category_id"],
                sku=row["sku"],
                name=row["name"],
                price=float(row["price"]),
                stock_quantity=int(row["stock_quantity"]),
                created_at=row["created_at"],
                updated_at=row["updated_at"],
            )
            for row in rows
        ]

    finally:

        connection.close()
