"""import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE College")
print("Database created successfully")"""
"""import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "College"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE Students (id INT, name VARCHAR(50))")
print("Table created successfully")"""
"""import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "College"
)
cursor = db.cursor()
sql ="INSERT INTO Students (id, name) VALUES (%s,%s)"
data = (1, "Balaji")
cursor.execute(sql, data)
db.commit()
print("Record inserted successfully")"""
"""import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "College"
)
cursor = db.cursor()
cursor.execute("SELECT * FROM Students")
for i in cursor.fetchall():
    print(i)
"""
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="College"
)
cursor = db.cursor()
sql = "UPDATE Students SET department=%s WHERE id=%s"
value = ("IT", 1)
cursor.execute(sql, value)
db.commit()
print(cursor.rowcount, "record updated")