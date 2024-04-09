from flask import Blueprint, render_template, request, redirect, url_for
from config.database import is_name_unique, insert_user, connect_to_database

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET', 'POST'])
def index():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            if is_name_unique(name):
                if insert_user(name):
                    return redirect(url_for('users.welcome'))
                else:
                    error_message = "Error occurred while processing the request."
            else:
                error_message = "Name already exists. Please choose a different name."
        else:
            error_message = "Name is required."

    return render_template('index.html', error_message=error_message)

@users_bp.route('/welcome')
def welcome():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name FROM users;")
            users = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template('temp.html', users=users)
        except Exception as e:
            print("Error fetching users:", e)
            connection.rollback()
            cursor.close()
            connection.close()
            return "Error occurred while fetching users."
    else:
        return "Failed to connect to the database."