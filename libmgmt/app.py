from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library_db"
    )

@app.route('/')
def home():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    db.close()
    return render_template("index.html", books=books)

@app.route('/issue', methods=['POST'])
def issue_book():
    book_id = request.form['book_id']
    member_id = request.form['member_id']

    db = get_db_connection()
    cursor = db.cursor()

    # Check if book is available
    cursor.execute("SELECT available_copies FROM Books WHERE book_id = %s", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        # Insert into Loans table
        cursor.execute("INSERT INTO Loans (book_id, member_id, loan_date, status) VALUES (%s, %s, CURDATE(), 'borrowed')", (book_id, member_id))
        # Update available copies
        cursor.execute("UPDATE Books SET available_copies = available_copies - 1 WHERE book_id = %s", (book_id,))
        db.commit()

    db.close()
    return redirect(url_for('home'))

