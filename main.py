import mysql.connector
from mysql.connector import Error
import os
import time
from datetime import datetime, timedelta

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    for _ in range(5):  # Try to connect up to 5 times
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
            break
        except Error as err:
            print(f"Error: '{err}'")
            time.sleep(5)  # Wait for 5 seconds before trying again

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

    return cursor

def main():
    # Establish connection
    host_name = os.environ.get('MYSQL_HOST')
    user_name = os.environ.get('MYSQL_USER')
    user_password = os.environ.get('MYSQL_PASSWORD')
    db_name = os.environ.get('MYSQL_DB')

    connection = create_server_connection(host_name, user_name, user_password, db_name)

    if connection is None:
        print("Failed: Could not connect to MySQL server.")
        return

    # Check Orders table exists
    cursor = execute_query(connection, "SHOW TABLES LIKE 'Orders';")
    result = cursor.fetchone()
    if result is None:
        print("Failed: 'Orders' table does not exist.")
        return

    # Check Orders table has at least 1000 rows
    cursor = execute_query(connection, "SELECT COUNT(*) FROM Orders;")
    result = cursor.fetchone()
    if result[0] < 1000:
        print("Failed: 'Orders' table does not contain at least 1000 records.")
        return

    # Test SELECT query
    customer_id = 21  # Adjust as necessary
    one_year_ago = (datetime.now() - timedelta(days=365)).date()
    cursor = execute_query(connection, f"SELECT * FROM Orders WHERE CustomerID = {customer_id} AND OrderDate > '{one_year_ago}';")
    results = cursor.fetchall()
    # Implement further checks based on your expected results here

    # Check if index exists and is used by the query
    cursor = execute_query(connection, f"EXPLAIN SELECT * FROM Orders WHERE CustomerID = {customer_id} AND OrderDate > '{one_year_ago}';")
    explain_result = cursor.fetchone()
    if explain_result[8] is None or explain_result[1] == "ALL":
        print("Failed: No index used in the SELECT query.")
        return

    print("Success: All checks passed.")

if __name__ == "__main__":
    main()
