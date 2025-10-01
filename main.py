from users import User
from database import Database
from getpass import getpass

db = Database()
user = User(db)
