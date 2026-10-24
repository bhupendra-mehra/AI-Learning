from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import TimestampMixin

if TYPE_CHECKING:
    from .order import Order


class Customer(TimestampMixin,Base):
    __tablename__ = "customers"

    id:Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email:Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    # Add inside your existing Customer model
    password_hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    orders:Mapped[list["Order"]] = relationship(
        back_populates="customer"
    )