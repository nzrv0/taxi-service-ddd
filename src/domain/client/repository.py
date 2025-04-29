from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create_client(self):
        pass

    @abstractmethod
    def delete_client(self, client_id):
        pass

    @abstractmethod
    def update_client_name(self, client_id):
        pass

    @abstractmethod
    def find_one_client(self, client_id):
        pass
