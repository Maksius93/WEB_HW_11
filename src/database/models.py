from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DATE
from sqlalchemy.orm import Mapped, mapped_column

from src.database.db import Base


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), index=True)
    surname: Mapped[str] = mapped_column(String(150), index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(20), index=True)
    bd: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    notes: Mapped[str] = mapped_column(String(300))