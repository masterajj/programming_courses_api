from app.database_connection import DatabaseConnection
from app.data_models import User

db = DatabaseConnection()
user = User(
    username="PS",
    password="123456",
    email="ps@email.com",
    country="Lithuania"
    )
db.insert_users(user)