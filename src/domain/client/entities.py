from src.domain.client.validators import (
    ClientValidator,
    RideValidator,
    AddressValidator,
)


class RideEntity(RideValidator):
    pass


class AddressEntity(AddressValidator):
    pass


class ClientEntity(ClientValidator):
    rides: list[RideEntity] = []
    addresses: list[AddressEntity] = []
