from user import User
from database import Database

class Student:
    def __init__(self,db):
        self.db = db 

    def add_student(self,name,dob,course,email):
        self.db.execute("INSERT INTO student (name,dob,course,email) VALUES (%s, %s, %s, %s)",
            (name,dob,course,email),
            commit = True
        )
        print(f"Student {name} has been added sucessfully")

    def update_student()