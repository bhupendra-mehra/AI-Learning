from unittest.mock import MagicMock

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository


def create_mock_session():
    return MagicMock()


def test_create_category():
    session = create_mock_session()
    repository = CategoryRepository(session)

    category = repository.create(
        name="Electronics",
        description="Electronic products",
    )

    assert isinstance(category, Category)
    assert category.name == "Electronics"
    assert category.description == "Electronic products"

    session.add.assert_called_once_with(category)
    session.flush.assert_called_once()


def test_update_category():
    session = create_mock_session()
    repository = CategoryRepository(session)

    category = Category(
        name="Electronics",
        description="Old description",
    )

    result = repository.update(
        category,
        name="Computers",
        description="Computer products",
    )

    assert result is category
    assert category.name == "Computers"
    assert category.description == "Computer products"

    session.flush.assert_called_once()


def test_delete_category():
    session = create_mock_session()
    repository = CategoryRepository(session)

    category = Category(
        name="Electronics",
        description="Electronic products",
    )

    repository.delete(category)

    session.delete.assert_called_once_with(category)
    session.flush.assert_called_once()