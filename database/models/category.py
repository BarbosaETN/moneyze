from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    budget: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0,
    )

    transactions = relationship(
        "Transaction",
        back_populates="category",
    )