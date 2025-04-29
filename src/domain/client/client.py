from src.domain.client.entities import ClientEntity


class Client:
    def __init__(self):
        self.client = ClientEntity

    def create(self, **kwargs):
        client = self.client(**kwargs)
        return dict(client)

    def delete(self, id):
        client = self.client(id=id)
        return dict(client)

    @staticmethod
    def update(id, full_name, email, addresses, rides):
        client = ClientEntity(id, full_name, email, addresses, rides)
        return client

    def add_ride(self, ride):
        self.rides.append(ride)

    def add_address(self, address):
        if address in self.addresses:
            return address
        self.addresses.add(address)
