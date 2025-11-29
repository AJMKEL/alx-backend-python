import sqlite3


class ExecuteQuery:
    """Class-based context manager for executing database queries"""
    
    def __init__(self, database, query, params=None):
        """
        Initialize the context manager with database, query, and parameters
        
        Args:
            database: Path to the SQLite database file
            query: SQL query string to execute
            params: Parameters to pass to the query (optional)
        """
        self.database = database
        self.query = query
        self.params = params if params is not None else ()
        self.connection = None
        self.cursor = None
        self.results = None
    
    def __enter__(self):
        """
        Open connection, execute query, and return results
        
        Returns:
            results: The query results (fetchall())
        """
        # Open database connection
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        
        # Execute the query with parameters
        self.cursor.execute(self.query, self.params)
        
        # Fetch and store results
        self.results = self.cursor.fetchall()
        
        return self.results
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close cursor and connection when exiting the context
        
        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        
        Returns:
            False to propagate exceptions (if any)
        """
        # Close cursor if it exists
        if self.cursor:
            self.cursor.close()
        
        # Close connection if it exists
        if self.connection:
            self.connection.close()
        
        # Return False to propagate any exceptions
        return False


if __name__ == "__main__":
    # Use the context manager to execute a query with parameters
    query = "SELECT * FROM users WHERE age > ?"
    
    with ExecuteQuery('users.db', query, (25,)) as results:
        print(f"Users older than 25:")
        for row in results:
            print(row)
