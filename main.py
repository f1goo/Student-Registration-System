from users import Users
from students import Students
from database import Database
from getpass import getpass

db = Database()
users = Users(db)
students = Students(db)

while True:
    print("\n1. Register\n2. Login\n3. Add Student\n4. Get student by ID\n5. Update Student details\n6. Delete Student\n7.Exit")
    choice = input("Select option: ")

    if choice == '1':
        username = input("Username: ")
        password = getpass("Password: ")
        users.register(username, password)

    elif choice == '2':
        username = input("Username: ")
        password = getpass("Enter password: ")
        if users.login(username, password):
            print("Login successful!")
        else:
            print("Invalid credentials")

    elif choice =='3':
        name = input("Enter name: ")
        dob = input("Enter DOB (dd-mm-yyyy): ")
        course = input("Enter course: ")
        email = input("Enter email: ")
        students.add_student(name,dob,course,email)

    elif choice == '4':
        student_id = input("Enter the student ID: ")
        students.get_student_ID(student_id)

    elif choice == '5':
        student_id = input("Enter the student ID: ")
        dob= input("Enter new DOB (leave blank to skip): ")
        course = input("Enter new course (leave blank to skip): ")
        email= input("Enter new email (leave blank to skip): ")
        students.update_student_details(student_id, dob, course, email)
        
    elif choice == '6':
        student_id = input("Enter the student ID: ")
        students.delete_student(student_id)

    elif choice == '7':
        break

    else:
        print("Invalid input.")