import datetime

from sqlalchemy import Date, Float, ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enums.transaction_type import TransactionType
from database.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    transaction_type: Mapped[TransactionType] = mapped_column(
        Enum(TransactionType),
        nullable=False
    )

    transaction_date: Mapped[datetime.date] = mapped_column(
        Date,
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category = relationship(
        "Category",
        back_populates="transactions"
    )

    