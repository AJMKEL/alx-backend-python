# Python Generators - Database Streaming Project

## Project Overview
This project demonstrates advanced usage of Python generators to efficiently handle large datasets by streaming rows from an SQL database one by one, promoting memory-efficient operations.

## Learning Objectives
- Master Python Generators for iterative data processing
- Handle large datasets with batch processing and lazy loading
- Integrate Python with MySQL for robust data management
- Implement memory-efficient database operations

## Project Structure
python-generators-0x00/
├── seed.py # Main database seeding and generator module
├── README.md # Project documentation
└── user_data.csv # Sample data file (to be provided)

text

## Database Schema
The project uses a MySQL database `ALX_prodev` with the following table:

### user_data Table
| Field    | Type         | Constraints               |
|----------|--------------|---------------------------|
| user_id  | VARCHAR(36)  | PRIMARY KEY, INDEXED      |
| name     | VARCHAR(255) | NOT NULL                  |
| email    | VARCHAR(255) | NOT NULL                  |
| age      | INT          | NOT NULL                  |

## Functions Overview

### `connect_db()`
- Connects to the MySQL database server
- Returns: MySQL connection object or None

### `create_database(connection)`
- Creates the `ALX_prodev` database if it doesn't exist
- Args: MySQL connection object

### `connect_to_prodev()`
- Connects specifically to the `ALX_prodev` database
- Returns: MySQL connection object or None

### `create_table(connection)`
- Creates the `user_data` table with required fields
- Args: MySQL connection object

### `insert_data(connection, csv_file_path)`
- Inserts data from CSV file into the database
- Prevents duplicate insertion
- Args: MySQL connection object, path to CSV file

### `stream_users_generator(connection, batch_size=100)`
- **Generator function** that streams rows one by one
- Uses batch processing for memory efficiency
- Yields individual user records
- Args: MySQL connection object, batch size

## Usage Example

```python
import seed

# Setup database and table
connection = seed.connect_db()
seed.create_database(connection)
connection.close()

connection = seed.connect_to_prodev()
seed.create_table(connection)
seed.insert_data(connection, 'user_data.csv')

# Use the generator to stream users
user_generator = seed.stream_users_generator(connection)

for user in user_generator:
    user_id, name, email, age = user
    print(f"Processing: {name} ({email})")
    # Process each user without loading all into memory
Memory Efficiency
The generator approach provides significant memory advantages:

Processes one record at a time

Doesn't load entire dataset into memory

Suitable for datasets of any size

Enables real-time processing of streaming data

Requirements
Python 3.x

mysql-connector-python

MySQL Server

CSV file with user data

Installation
bash
pip install mysql-connector-python
Configuration
Update database credentials in seed.py:

python
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='ALX_prodev'
)
Features
✅ Database connection management

✅ Automatic database and table creation

✅ CSV data import with duplicate prevention

✅ Memory-efficient generator for data streaming

✅ Batch processing for large datasets

✅ Error handling and logging

This project demonstrates practical application of Python generators for efficient database operations in real-world scenarios.

text

## Additional Notes:

1. **MySQL Setup**: Make sure you have MySQL installed and running on your system.

2. **Dependencies**: Install the required package:
   ```bash
   pip install mysql-connector-python
CSV File: You'll need to create a user_data.csv file with the following format:

text
user_id,name,email,age
uuid1,John Doe,john@example.com,30
uuid2,Jane Smith,jane@example.com,25
... (more records)
Database Credentials: Update the connection parameters in seed.py to match your MySQL setup.

The generator function stream_users_generator is the key component that demonstrates memory-efficient data streaming by yielding one row at a time instead of loading all data into memory.
