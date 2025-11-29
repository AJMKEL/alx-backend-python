import sqlite3
import functools


def log_queries(func):
    """Decorator to log SQL queries before executing them"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from arguments
        # Check if 'query' is in kwargs
        if 'query' in kwargs:
            query = kwargs['query']
        # Otherwise, assume it's the first positional argument
        elif args:
            query = args[0]
        else:
            query = "No query provided"
        
        # Log the query
        print(f"Executing query: {query}")
        
        # Execute the original function
        return func(*args, **kwargs)
    
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(f"Fetched {len(users)} users")
