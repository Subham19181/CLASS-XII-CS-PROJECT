#Program 23
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19181",
    database="school"
)
cursor = db.cursor()

while True:
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    query = "INSERT INTO student (name, age, subject, marks)VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, age, subject, marks))
    ch = input("Do you want to insert more records? (Y/N)")
    if ch == 'n' or ch == 'N':
        break
     
    
db.commit()
print("Record inserted successfully.")
    
cursor.close()
db.close()