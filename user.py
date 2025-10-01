import hashlib
from database import Database
import mysql.connector

class User:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        result = self.db.execute("SELECT * FROM users WHERE username=%s", (username,)).fetchone()
        if result:
            print("Username already exists")
        else:
            self.db.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed),
                commit=True
            )
            print("User registered successfully")

    def login(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
