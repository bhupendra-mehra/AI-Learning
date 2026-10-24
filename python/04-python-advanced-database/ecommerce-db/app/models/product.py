from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .category import Category
    from .order_item import OrderItem


class Product(TimestampMixin , Base):
    __tablename__ = "products"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name : Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    sku:Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
   
    price: Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )

    category_id:Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )


