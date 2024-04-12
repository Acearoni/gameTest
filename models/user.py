from config.database import connect_to_database, insert_user, is_name_unique

class User:
    @staticmethod
    def is_name_unique(name):
        return is_name_unique(name)

    @staticmethod
    def insert_user(name):
        return insert_user(name)