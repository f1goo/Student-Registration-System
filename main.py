from user import User
from database import Database
from getpass import getpass

db = Database()
user = User(db)

while True:
    print("\n1. Register\n2. Login\n3. Exit")
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

    elif choice == '3':
        break
    else:
        print("Invalid input.")