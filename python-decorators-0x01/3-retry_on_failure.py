import time
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


def retry_on_failure(retries=3, delay=2):
    """Decorator to retry database operations on failure"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(retries):
                try:
                    # Attempt to execute the function
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    
                    # Don't delay after the last attempt
                    if attempt < retries - 1:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
            
            # If all retries failed, raise the last exception
            print(f"All {retries} attempts failed.")
            raise last_exception
        
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# Attempt to fetch users with automatic retry on failure
if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(users)
