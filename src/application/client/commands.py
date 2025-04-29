from src.application.common.command import Command
from src.infrastructure.persistence.repositories.client_repository import (
    ClientRepository,
)


class CreateClientCommand(Command):
    def __init__(self):
        self.client = ClientRepository()

    def execute(self, data):
        self.client.create_client(data=data)


class DeleteClientCommand(Command):
    def __init__(self):
        self.client = ClientRepository()

    def execute(self, id):
        self.client.delete_client(id)


class UpdateClientInformationsCommand(Command):
    def __init__(self):
        self.client = ClientRepository()

    def execute(self, id, full_name):
        self.client.update_client_name(id, full_name)


class TakeRideCommand(Command):
    def __init__(self):
        self.client = ClientRepository()

    def execute(self):
        self.client.take_ride()


class CancelRideCommand(Command):
    def __init__(self):
        self.client = ClientRepository()

    def execute(self):
        self.client.cancel_ride()
