from src.application.client.handlers import Handler
from src.infrastructure.database import connect

full_name = "john watson"
email = "john.watson@gmail.com"

response = Handler.create_client(full_name, email)
print(response)
