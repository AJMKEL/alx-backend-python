#!/usr/bin/python3
from seed import connect_to_prodev

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    connection = connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    
    for row in cursor:  # single loop
        yield row['age']
    
    cursor.close()
    connection.close()


def calculate_average_age():
    """Calculates the average age using the generator without loading all data into memory."""
    total = 0
    count = 0

    for age in stream_user_ages():  # second loop
        total += age
        count += 1

    if count == 0:
        return 0
    return total / count


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
