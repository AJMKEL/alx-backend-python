import sqlite3
import functools


def with_db_connection(func):
    """Decorator to automatically handle database connections"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open database connection
        conn = sqlite3.connect('users.db')
        
        try:
            # Pass connection to the function
            result = func(conn, *args, **kwargs)
            return result
        finally:
            # Always close the connection
            conn.close()
    
    return wrapper


def transactional(func):
    """Decorator to manage database transactions with commit/rollback"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the function
            result = func(conn, *args, **kwargs)
            # If successful, commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # If error occurs, rollback the transaction
            conn.rollback()
            # Re-raise the exception for proper error handling
            raise e
    
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


# Update user's email with automatic transaction handling
if __name__ == "__main__":
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print("User email updated successfully")
