#Program 24

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19181",
    database="school"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM student")
students = cursor.fetchall()

for student in students:
    print(student)

cursor.close()
db.close()