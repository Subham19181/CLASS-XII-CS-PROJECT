#Program 26

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19181",
    database="school"
)

cursor = db.cursor()

name = input("Enter the name of the student to update: ")
new_marks = int(input("Enter the new marks: "))
query = "UPDATE student SET marks = %s WHERE name = %s"
cursor.execute(query, (new_marks, name))
db.commit()
print("Record updated successfully.")
    
cursor.close()
db.close()