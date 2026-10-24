from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .customer import Customer
    from .order_item import OrderItem


class Order(TimestampMixin,Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
       ForeignKey("customers.id"),
       nullable=False
    )

    status : Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending"
    )

    total_amount : Mapped[Decimal] = mapped_column(
        Numeric(12,2),
        nullable=False,
        default=0
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order"
    )

    