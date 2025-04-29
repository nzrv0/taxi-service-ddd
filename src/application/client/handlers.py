from src.application.client.commands import CreateClientCommand, DeleteClientCommand
from src.domain.client.client import Client
from src.application.client.exceptions import (
    UserNotFound,
    CannotCreateUser,
    CannotDeleteUser,
)
from src.application.client.queries import GetClient


class Handler:
    @staticmethod
    def create_client(full_name, email):
        try:
            client = GetClient().get_client_by_name(client_name=full_name)
            if not client:
                client_info = Client().create(full_name=full_name, email=email)
                command = CreateClientCommand().execute(client_info)
                return command
        except CannotCreateUser as err:
            raise err

    def delete_handler(self, client_id):
        try:
            client = self.client.find_one_client(client_id=client_id)
            if not client:
                command = DeleteClientCommand(self.client)
                command.execute(client_id)
        except CannotDeleteUser as err:
            raise err

    # def update_name_handler(self, client_id, full_name):
    #     try:
    #         client = self.client.find_one_client(client_id)
    #         if not client:
    #             command = UpdateClientCommand(self.client)
    #             command.execute(client_id)
    #     except CannotDeleteUser as err:
    #         raise err
