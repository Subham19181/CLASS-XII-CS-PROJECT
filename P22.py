#Program 22

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="19181",
    database="school"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    subject VARCHAR(100),
    marks INT
)
""")
print("Student table created successfully.")

cursor.close()
db.close()