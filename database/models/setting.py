from sqlalchemy import (
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from database.base import Base


class Setting(Base):

    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    key: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )