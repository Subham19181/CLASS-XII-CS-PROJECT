import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19181",
    database="school"
)

cursor = db.cursor()

name = input("Enter the name of the student to delete: ")
query = "DELETE FROM student WHERE name = %s"
cursor.execute(query, (name,))
db.commit()
print("Record deleted successfully.")
    

cursor.close()
db.close()