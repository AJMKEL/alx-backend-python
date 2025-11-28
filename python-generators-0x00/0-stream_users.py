#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev

def stream_users():
    """Generator that yields rows from user_data table one by one as dictionaries."""
    connection = connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)  # dictionary=True returns rows as dict
    cursor.execute("SELECT * FROM user_data;")

    for row in cursor:  # single loop over cursor
        yield row

    cursor.close()
    connection.close()
