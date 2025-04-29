from pydantic import BaseModel, ConfigDict, EmailStr, StringConstraints, Field
import uuid
from datetime import datetime
from typing import Annotated


class ClientValidator(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID = Field(default_factory=uuid.uuid1)
    full_name: Annotated[str, StringConstraints(min_length=5, max_length=50)]
    email: EmailStr


class RideValidator(BaseModel):
    ride_time: datetime = Field(default_factory=datetime.now)
    address: str
    cost: float
    cash: bool


class AddressValidator(BaseModel):
    address_name: str
