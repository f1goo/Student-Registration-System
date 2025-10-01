import hashlib
from database import Database
import mysql.connector

class User:
    def __init__(self, db):
        self.db = db



    def register(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
    
    def login(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
