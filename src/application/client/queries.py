from src.infrastructure.persistence.repositories.client_repository import ClientRepository


class GetClient:
    def __init__(self):
        self.client = ClientRepository()

    def get_client_by_name(self, client_name):
        client = self.client.find_one_client(client_name=client_name)
        return client
