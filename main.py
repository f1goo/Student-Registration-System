from user import User
from database import Database
from getpass import getpass

db = Database()
user = User(db)

print("1. Register")