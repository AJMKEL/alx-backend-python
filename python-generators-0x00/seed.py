#!/usr/bin/python3
"""
Database Seeding Module for ALX Python Generators Project
"""

import mysql.connector
import csv
import uuid
import os
from mysql.connector import Error


def connect_db():
    """
    Connects to the MySQL database server
    
    Returns:
        connection: MySQL connection object or None if failed
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change as per your MySQL setup
            password=''   # Change as per your MySQL setup
        )
        if connection.is_connected():
            print("Connected to MySQL server successfully")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """
    Creates the database ALX_prodev if it does not exist
    
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """
    Connects to the ALX_prodev database in MySQL
    
    Returns:
        connection: MySQL connection object or None if failed
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',      # Change as per your MySQL setup
            password='',      # Change as per your MySQL setup
            database='ALX_prodev'
        )
        if connection.is_connected():
            print("Connected to ALX_prodev database successfully")
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    """
    Creates a table user_data if it does not exist with the required fields
    
    Args:
        connection: MySQL connection object
    """
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """
        cursor.execute(create_table_query)
        print("Table user_data created successfully")
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file_path):
    """
    Inserts data in the database from CSV file if it does not exist
    
    Args:
        connection: MySQL connection object
        csv_file_path: Path to the CSV file containing user data
    """
    try:
        # Check if data already exists to avoid duplicates
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user_data")
        count = cursor.fetchone()[0]
        
        if count > 0:
            print("Data already exists in the table. Skipping insertion.")
            cursor.close()
            return
        
        # Read and insert data from CSV
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            
            insert_query = """
            INSERT IGNORE INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """
            
            data_to_insert = []
            for row in csv_reader:
                if len(row) >= 4:
                    user_id = row[0] if row[0] else str(uuid.uuid4())
                    name = row[1]
                    email = row[2]
                    try:
                        age = int(row[3])
                    except ValueError:
                        age = 0  # Default value if age is not valid
                    
                    data_to_insert.append((user_id, name, email, age))
            
            # Insert in batches to handle large datasets
            batch_size = 100
            for i in range(0, len(data_to_insert), batch_size):
                batch = data_to_insert[i:i + batch_size]
                cursor.executemany(insert_query, batch)
                connection.commit()
            
            print(f"Inserted {len(data_to_insert)} records successfully")
        
        cursor.close()
        
    except FileNotFoundError:
        print(f"CSV file {csv_file_path} not found")
    except Error as e:
        print(f"Error inserting data: {e}")


def stream_users_generator(connection, batch_size=100):
    """
    Generator function that streams rows from user_data table one by one
    
    Args:
        connection: MySQL connection object
        batch_size: Number of rows to fetch at a time
    
    Yields:
        tuple: A row from the user_data table
    """
    try:
        cursor = connection.cursor()
        
        # Get total count for progress tracking
        cursor.execute("SELECT COUNT(*) FROM user_data")
        total_rows = cursor.fetchone()[0]
        
        print(f"Streaming {total_rows} users...")
        
        # Fetch data in batches using generator approach
        offset = 0
        while True:
            cursor.execute(
                "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s",
                (batch_size, offset)
            )
            
            batch = cursor.fetchall()
            if not batch:
                break
            
            for row in batch:
                yield row
            
            offset += batch_size
            print(f"Processed {min(offset, total_rows)}/{total_rows} users")
        
        cursor.close()
        
    except Error as e:
        print(f"Error streaming users: {e}")


if __name__ == "__main__":
    # Test the functions
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()
        
        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            # You'll need to provide the actual path to user_data.csv
            insert_data(connection, 'user_data.csv')
            
            # Test the generator
            print("\nTesting generator function:")
            user_gen = stream_users_generator(connection, batch_size=50)
            count = 0
            for user in user_gen:
                print(f"User {count + 1}: {user}")
                count += 1
                if count >= 5:  # Show first 5 users as example
                    break
            
            connection.close()
