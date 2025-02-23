import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library_db"
)

cursor = db.cursor()

# Insert a new book
insert_query = "INSERT INTO Books (title, author, genre, total_copies, available_copies) VALUES (%s, %s, %s, %s, %s)"
book_data = ("Python Programming", "Guido van Rossum", "Technology", 5, 5)

cursor.execute(insert_query, book_data)
db.commit()

print("New book inserted successfully!")

db.close()
