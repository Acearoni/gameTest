from config.database import connect_to_database

class User:
    @staticmethod
    def is_name_unique(name):
        connection = connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id FROM users WHERE LOWER(name) = LOWER(%s);", (name,))
                    existing_user = cursor.fetchone()
                    return not existing_user
            except Exception as e:
                print("Error checking name uniqueness:", e)
            finally:
                connection.close()
        return False

    @staticmethod
    def insert_user(name):
        if not User.is_name_unique(name):
            print("Name already exists. Insertion aborted.")
            return False

        connection = connect_to_database()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO users (name) VALUES (%s);", (name,))
                    connection.commit()
                    return True
            except Exception as e:
                print("Error inserting user:", e)
            finally:
                connection.close()
        return False
