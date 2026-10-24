from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.utils.pagination import Pagination


class CustomerRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        name: str,
        email: str,
        password_hash: str | None = None,
    ) -> Customer | None:

        customer = Customer(name=name, email=email, password_hash=password_hash)
        self.session.add(customer)
        self.session.flush()
        return customer

    def get_by_id(self, customer_id: int) -> Customer | None:

        return self.session.get(Customer, customer_id)

    def get_by_email(self, email: str) -> Customer:

        statement = select(Customer).where(Customer.email == email)

        return self.session.scalars(statement).first()

    def get_all(
        self,
        page: int = 1,
        per_page: int = 10,
    ) -> Pagination[Customer]:

        page = max(page, 1)
        per_page = max(per_page, 1)
        offset = (page - 1) * per_page

        statement = (
            select(Customer).order_by(Customer.id.desc()).offset(offset).limit(per_page)
        )

        customers = list(self.session.scalars(statement).all())

        count_statement = select(func.count()).select_from(Customer)

        total = self.session.scalar(count_statement) or 0

        return Pagination(
            items=customers,
            page=page,
            per_page=per_page,
            total=total,
        )

    def update(self, customer: Customer, name: str, email: str) -> Customer | None:
        customer.name = name
        customer.email = email

        # self.session.commit()
        self.session.flush()

        return customer

    def delete(self, customer: Customer) -> bool:

        self.session.delete(customer)
        self.session.flush()

        return True
