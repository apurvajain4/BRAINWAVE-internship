import mysql.connector  # Add this line to import MySQL connector
def return_book(loan_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="library_db"
    )
    cursor = db.cursor()

    # Get book_id from the loan record
    cursor.execute("SELECT book_id FROM Loans WHERE loan_id = %s AND status = 'borrowed'", (loan_id,))
    result = cursor.fetchone()

    if result:
        book_id = result[0]
        
        # Update loan status to 'returned'
        return_query = "UPDATE Loans SET status = 'returned', return_date = CURDATE() WHERE loan_id = %s"
        cursor.execute(return_query, (loan_id,))
        
        # Update available copies
        update_query = "UPDATE Books SET available_copies = available_copies + 1 WHERE book_id = %s"
        cursor.execute(update_query, (book_id,))
        
        db.commit()
        print("Book returned successfully!")
    else:
        print("Invalid loan ID or book already returned.")

    db.close()

# Example usage
return_book(1)  # Return book with loan ID 1
