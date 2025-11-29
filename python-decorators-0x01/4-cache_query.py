import time
import sqlite3
import functools


query_cache = {}


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


def cache_query(func):
    """Decorator to cache database query results"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from arguments
        # Check if 'query' is in kwargs
        if 'query' in kwargs:
            query = kwargs['query']
        # Otherwise, check positional arguments (skip conn which is first)
        elif len(args) > 1:
            query = args[1]
        else:
            query = None
        
        # If query is found, check cache
        if query:
            if query in query_cache:
                print("Using cached result for query:", query)
                return query_cache[query]
        
        # Execute the function if not cached
        print("Executing query and caching result:", query)
        result = func(*args, **kwargs)
        
        # Cache the result
        if query:
            query_cache[query] = result
        
        return result
    
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
if __name__ == "__main__":
    print("First call:")
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Fetched {len(users)} users\n")
    
    # Second call will use the cached result
    print("Second call:")
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Fetched {len(users_again)} users")
