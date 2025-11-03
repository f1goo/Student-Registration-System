from users import Users
from database import Database

class Students:
    def __init__(self,db):
        self.db = db 

    def add_student(self,name,dob,course,email):
        self.db.execute("INSERT INTO students (name,dob,course,email) VALUES (%s, %s, %s, %s)",
            (name,dob,course,email),
            commit = True
        )
        print(f"Student {name} has been added sucessfully")

    def get_student_ID(self,student_id):
        result = self.db.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (student_id,)
        ).fetchone()
        if result:
            print(f"Student found",result)
            return True
        else:
            print(f"No student with the student id {student_id}")
            return False

    def update_student_details(self, student_id, dob=None, course=None, email=None):
        query = "UPDATE students SET"
        values = []
        updates = []

        if dob:
            updates.append("dob = %s")
            values.append(dob)
        if course:
            updates.append("course = %s")
            values.append(course)
        if email:
            updates.append("email = %s")
            values.append(email)
        
        if not updates:
            print("No fields to update.")
            return
        query = f"UPDATE student SET { ",".join(updates)} WHERE student_id = %s"
        values.append(student_id)

        self.db.execute(query, tuple(values),commit=True)
        print(f"Student {student_id} updated successfully!")

    def delete_student(self, student_id):
        result = self.db.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id,)
        )
        if result:
            print(f"Student {student_id} deleted successfully", result)
        else:
            print(f"No student found with the student id: {student_id}")