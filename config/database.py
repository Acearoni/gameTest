# config/database.py

import psycopg2
from psycopg2 import Error

# Database connection function
def connect_to_database():
    try:
        # Modify these parameters with your database connection details
        connection = psycopg2.connect(
            user="postgres",
            password="4654",
            host="localhost",
            port="5432",
            database="gameDB"
        )
        print("Successfully connected to PostgreSQL")
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

# Function to execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except (Exception, Error) as error:
        print("Error executing query:", error)
    finally:
        cursor.close()
