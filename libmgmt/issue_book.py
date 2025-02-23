import mysql.connector  # Add this line to import MySQL connector

def issue_book(book_id, member_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library_db"
    )
    cursor = db.cursor()

    # Check if the book is available
    cursor.execute("SELECT available_copies FROM Books WHERE book_id = %s", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        # Insert into Loans table
        issue_query = "INSERT INTO Loans (book_id, member_id, loan_date, status) VALUES (%s, %s, CURDATE(), 'borrowed')"
        cursor.execute(issue_query, (book_id, member_id))
        
        # Update available copies
        update_query = "UPDATE Books SET available_copies = available_copies - 1 WHERE book_id = %s"
        cursor.execute(update_query, (book_id,))
        
        db.commit()
        print("Book issued successfully!")
    else:
        print("Book is not available.")

    db.close()

# Example usage
issue_book(1, 1)  # Issue book with ID 1 to member with ID 1
