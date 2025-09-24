import mysql.connector
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2121',
            database='student_db'
        )
        self.cursor = self.conn.cursor(dictionary=True)
