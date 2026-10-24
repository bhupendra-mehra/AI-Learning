from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.models.product import Product
from app.utils.pagination import Pagination


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_products(self):
        statement = select(Product).order_by(Product.id)
        return self.session.scalars(statement).all()

    def get_all(
        self,
        page: int = 1,
        per_page: int = 10,
    ) -> Pagination[Product]:

        page = max(page, 1)
        per_page = max(per_page, 1)
        offset = (page - 1) * per_page

        statement = (
            select(Product).order_by(Product.id.desc()).offset(offset).limit(per_page)
        )

        products = list(self.session.scalars(statement).all())

        count_statement = select(func.count()).select_from(Product)

        total = self.session.scalar(count_statement) or 0

        return Pagination(
            items=products,
            page=page,
            per_page=per_page,
            total=total,
        )

    def get_by_id(self, product_id: int):
        statement = (
            select(Product)
            .options(selectinload(Product.category))
            .where(Product.id == product_id)
        )
        return self.session.scalar(statement)

    def create(
        self,
        name: str,
        sku: str | None,
        price,
        quantity: int,
        category_id: int,
    ):
        product = Product(
            name=name,
            sku=sku,
            price=price,
            quantity=quantity,
            category_id=category_id,
        )
        self.session.add(product)
        self.session.flush()
        return product

    def update(self, product: Product, **values):
        for field, value in values.items():
            setattr(product, field, value)

        self.session.flush()
        return product

    def delete(self, product: Product):
        self.session.delete(product)
        self.session.flush()

    def get_by_category(self, category_id: int):
        statement = (
            select(Product)
            .options(selectinload(Product.category))
            .where(Product.category_id == category_id)
            .order_by(Product.name)
        )
        return self.session.scalars(statement).all()
