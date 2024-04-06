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
    
    
def is_name_unique(name):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Check if the name already exists in a case-insensitive manner
            cursor.execute("SELECT id FROM users WHERE LOWER(name) = LOWER(%s);", (name,))
            existing_user = cursor.fetchone()

            cursor.close()
            connection.close()

            return not existing_user  # Return True if name is unique, False if already exists
        
        except Exception as e:
            print("Error checking name uniqueness:", e)
            connection.rollback()
            cursor.close()
            connection.close()
    
    return False  # Default to False if unable to check

def insert_user(name):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()

            # Insert the new user into the users table
            cursor.execute("INSERT INTO users (name) VALUES (%s);", (name,))
            connection.commit()

            cursor.close()
            connection.close()

            return True  # Return True on successful insertion
        
        except Exception as e:
            print("Error inserting user:", e)
            connection.rollback()
            cursor.close()
            connection.close()
    
    return False  # Default to False if insertion fails
