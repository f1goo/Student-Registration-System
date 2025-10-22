from user import User
from student import Student
from database import Database
from getpass import getpass

db = Database()
user = User(db)
student = Student(db)

while True:
    print("\n1. Register\n2. Login\n3. Add Student\n4.Exit")
    choice = input("Select option: ")

    if choice == '1':
        username = input("Username: ")
        password = getpass("Password: ")
        user.register(username, password)

    elif choice == '2':
        username = input("Username: ")
        password = getpass("Enter password: ")
        if user.login(username, password):
            print("Login successful!")
        else:
            print("Invalid credentials")

    elif choice =='3':
        name = input("Enter name: ")
        dob = input("Enter DOB (dd-mm-yyyy): ")
        course = input("Enter course: ")
        email = input("Enter email: ")
        student.add_student(name,dob,course,email)

    elif choice == '4':
        break
    else:
        print("Invalid input.")