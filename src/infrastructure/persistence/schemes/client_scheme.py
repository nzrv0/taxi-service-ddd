from src.infrastructure.persistence.common.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid


class ClientScheme(Base):
    __tablename__ = "client"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(60))
    addresses: Mapped[list["AddressScheme"]] = relationship(
        "AddressScheme", backref="client"
    )
    rides: Mapped[list["RideScheme"]] = relationship("RideScheme", backref="client")


class AddressScheme(Base):
    __tablename__ = "address"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    _client_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("client.id"))

    rides: Mapped[list["RideScheme"]] = relationship("RideScheme", backref="address")


class RideScheme(Base):
    __tablename__ = "ride"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    ride_time: Mapped[str] = mapped_column(primary_key=True)
    cost: Mapped[float]
    cash: Mapped[bool]

    _client_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("client.id"))

    _address_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("address.id"))
