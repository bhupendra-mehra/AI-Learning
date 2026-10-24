from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.category import Category
from app.utils.pagination import Pagination


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_categories(self):
        statement = select(Category).order_by(Category.id)
        return self.session.scalars(statement).all()

    def get_all(
        self,
        page: int = 1,
        per_page: int = 10,
    ) -> Pagination[Category]:

        page = max(page, 1)
        per_page = max(per_page, 1)
        offset = (page - 1) * per_page

        statement = (
            select(Category).order_by(Category.id.desc()).offset(offset).limit(per_page)
        )

        categories = list(self.session.scalars(statement).all())

        count_statement = select(func.count()).select_from(Category)

        total = self.session.scalar(count_statement) or 0

        return Pagination(
            items=categories,
            page=page,
            per_page=per_page,
            total=total,
        )

    def get_by_id(self, category_id: int):
        return self.session.get(Category, category_id)

    def get_by_name(self, name: str):
        statement = select(Category).where(Category.name == name)
        return self.session.scalar(statement)

    def create(self, name: str, description: str | None = None):
        category = Category(
            name=name,
            description=description,
        )
        self.session.add(category)
        self.session.flush()
        return category

    def update(
        self,
        category: Category,
        name: str,
        description: str | None = None,
    ):
        category.name = name
        category.description = description
        self.session.flush()
        return category

    def delete(self, category: Category):
        self.session.delete(category)
        self.session.flush()
