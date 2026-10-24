from unittest.mock import MagicMock

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


def test_get_all_products():
    session = MagicMock()
    repository = ProductRepository(session)

    product1 = Product(
        id=2,
        name="Mouse",
        sku="MOU-001",
        price=100,
        quantity=10,
        category_id=1,
    )

    product2 = Product(
        id=1,
        name="Keyboard",
        sku="KEY-001",
        price=200,
        quantity=5,
        category_id=1,
    )

    session.scalars.return_value.all.return_value = [
        product1,
        product2,
    ]

    session.scalar.return_value = 2

    result = repository.get_all(page=1, per_page=10)

    assert result.items == [product1, product2]
    assert result.page == 1
    assert result.per_page == 10
    assert result.total == 2


def test_get_all_products_corrects_invalid_page():
    session = MagicMock()
    repository = ProductRepository(session)

    session.scalars.return_value.all.return_value = []
    session.scalar.return_value = 0

    result = repository.get_all(page=0, per_page=0)

    assert result.page == 1
    assert result.per_page == 1
    assert result.total == 0