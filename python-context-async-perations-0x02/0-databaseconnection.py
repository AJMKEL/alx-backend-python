import sqlite3


class DatabaseConnection:
    """Class-based context manager for database connections"""
    
    def __init__(self, database):
        """
        Initialize the context manager with database path
        
        Args:
            database: Path to the SQLite database file
        """
        self.database = database
        self.connection = None
    
    def __enter__(self):
        """
        Open database connection when entering the context
        
        Returns:
            connection: The database connection object
        """
        self.connection = sqlite3.connect(self.database)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close database connection when exiting the context
        
        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        
        Returns:
            False to propagate exceptions (if any)
        """
        if self.connection:
            self.connection.close()
        # Return False to propagate any exceptions that occurred
        return False


if __name__ == "__main__":
    # Use the context manager to perform a query
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        
        # Print the results
        print("Users:")
        for row in results:
            print(row)
