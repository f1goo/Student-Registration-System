from users import Users
from students import Students
from database import Database
from getpass import getpass

db = Database()
users = Users(db)
students = Students(db)

while True:
    print("\n----------------------------\n1. | Register\n2. | Login\n3. | Add Student\n4. | Search Student\n5. | Update Student details\n6. | Delete Student\n7. | View all students\n8. | Exit\n----------------------------\n")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Username: ")
        password = getpass("Password: ")
        users.register(username, password)

    elif choice == "2":
        username = input("Username: ")
        password = getpass("Password: ")
        if users.login(username, password):
            print("Login successful!")
        else:
            print("Invalid information, please recheck username and password.")

    elif choice =="3":
        name = input("Enter full name: ")
        dob = input("Enter DOB (dd-mm-yyyy): ")
        course = input("Enter course: ")
        email = input("Enter email: ")
        students.add_student(name,dob,course,email)

    elif choice == "4":
        print("\n----------\n1. | ID\n2. | Name\n----------\n")
        search_choice = input("Select option:")
        if search_choice == "1":
            student_id = input("Enter the student ID: ")
            students.get_student_ID(student_id)
        elif search_choice == "2":
            student_name=input("Enter the student Name: ")
            students.get_student_Name(student_name)
        else:
            print("Invalid choice.")

    elif choice == "5":
        student_id = input("Enter the student ID: ")
        dob= input("Enter new DOB (leave blank to skip): ")
        course = input("Enter new course (leave blank to skip): ")
        email= input("Enter new email (leave blank to skip): ")
        students.update_student_details(student_id, dob, course, email)

    elif choice == "6":
        student_id = input("Enter the student ID: ")
        students.delete_student(student_id)

    elif choice == "7":
        students.view_students()

    elif choice == "8":
        break

    else:
        print("Invalid choice.")