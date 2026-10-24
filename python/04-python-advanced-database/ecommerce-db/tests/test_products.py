from decimal import Decimal
from unittest.mock import MagicMock

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


def create_mock_session():
    return MagicMock()


def test_create_product():
    session = create_mock_session()
    repository = ProductRepository(session)

    product = repository.create(
        name="Laptop",
        sku="LAP-001",
        price=Decimal("999.99"),
        quantity=10,
        category_id=1,
    )

    assert isinstance(product, Product)
    assert product.name == "Laptop"
    assert product.sku == "LAP-001"
    assert product.price == Decimal("999.99")
    assert product.quantity == 10
    assert product.category_id == 1

    session.add.assert_called_once_with(product)
    session.flush.assert_called_once()


def test_update_product():
    session = create_mock_session()
    repository = ProductRepository(session)

    product = Product(
        name="Laptop",
        sku="LAP-001",
        price=Decimal("999.99"),
        quantity=10,
        category_id=1,
    )

    result = repository.update(
        product,
        price=Decimal("899.99"),
        quantity=8,
    )

    assert result is product
    assert product.price == Decimal("899.99")
    assert product.quantity == 8

    session.flush.assert_called_once()


def test_delete_product():
    session = create_mock_session()
    repository = ProductRepository(session)

    product = Product(
        name="Laptop",
        sku="LAP-001",
        price=Decimal("999.99"),
        quantity=10,
        category_id=1,
    )

    repository.delete(product)

    session.delete.assert_called_once_with(product)
    session.flush.assert_called_once()