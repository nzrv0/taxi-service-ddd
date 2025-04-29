from src.domain.client.repository import Repository
from src.infrastructure.persistence.schemes.client_scheme import ClientScheme
from sqlalchemy.orm import Session

from src.infrastructure.database import connect


class ClientRepository(Repository):
    client = ClientScheme

    @connect
    def create_client(self, session: Session, data):
        client = self.client(**data)
        session.add(client)

    def delete_client(self, client):
        action = self.session.delete(client)
        self.session.execute(action)

    def update_client_name(self, client, full_name):
        client.full_name = full_name

    @connect
    def find_one_client(self, session: Session, client_name):
        client = (
            session.query(self.client)
            .where(self.client.full_name == client_name)
            .first()
        )
        return client
