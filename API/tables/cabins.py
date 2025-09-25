from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Table, Column
from basic.table import BaseTable


# --- Association tables ---
cabine_media_association = Table(
    "cabine_media_association",
    BaseTable.metadata,
    Column("cabine_id", ForeignKey("cabines.id"), primary_key=True),
    Column("media_id", ForeignKey("cabine_media.id"), primary_key=True),
)

booking_amenity_association = Table(
    "booking_amenity_association",
    BaseTable.metadata,
    Column("booking_id", ForeignKey("cabine_bookings.id"), primary_key=True),
    Column("amenity_id", ForeignKey("cabine_amenities.id"), primary_key=True),
)


# --- Tables ---
class CabineClass(BaseTable):
    __tablename__ = "cabine_classes"

    cabine_class: Mapped[str]
    description: Mapped[str | None]

    cabins = relationship("Cabine", back_populates="cabine_class")


class Cabine(BaseTable):
    __tablename__ = "cabines"

    number: Mapped[int]
    description: Mapped[str | None]
    price: Mapped[float]
    capacity: Mapped[int]

    cabine_class_id: Mapped[int] = mapped_column(ForeignKey("cabine_classes.id"))
    cabine_class = relationship("CabineClass", back_populates="cabins")

    amenities = relationship("CabineAmenity", back_populates="cabine")
    bookings = relationship("CabineBooking", back_populates="cabine")
    media = relationship("CabineMedia", secondary=cabine_media_association, back_populates="cabins")


class CabineMedia(BaseTable):
    __tablename__ = "cabine_media"

    media: Mapped[str]

    cabins = relationship("Cabine", secondary=cabine_media_association, back_populates="media")


class CabineAmenity(BaseTable):
    __tablename__ = "cabine_amenities"

    cabine_id: Mapped[int] = mapped_column(ForeignKey("cabines.id"))
    amenity: Mapped[str]
    price: Mapped[float]
    image: Mapped[str]
    is_available: Mapped[bool]
    description: Mapped[str | None]

    cabine = relationship("Cabine", back_populates="amenities")
    bookings = relationship("CabineBooking", secondary=booking_amenity_association, back_populates="amenities")


class CabineBooking(BaseTable):
    __tablename__ = "cabine_bookings"

    cabine_id: Mapped[int] = mapped_column(ForeignKey("cabines.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    total_price: Mapped[float]

    cabine = relationship("Cabine", back_populates="bookings")
    user = relationship("UserTable", back_populates="cabine_bookings")
    amenities = relationship("CabineAmenity", secondary=booking_amenity_association, back_populates="bookings")
