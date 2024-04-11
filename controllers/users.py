from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET', 'POST'])
def index():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            if User.is_name_unique(name):
                if User.insert_user(name):
                    flash("User successfully added!", "success")
                    return redirect(url_for('users.temp'))
                else:
                    error_message = "Error occurred while processing the request."
            else:
                error_message = "Name already exists. Please choose a different name."
        else:
            error_message = "Name is required."

    return render_template('index.html', error_message=error_message)

@users_bp.route('/temp')
def temp():
    from config.database import connect_to_database

    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name FROM users;")
                users = cursor.fetchall()
                return render_template('temp.html', users=users)
        except Exception as e:
            print("Error fetching users:", e)
        finally:
            connection.close()
    flash("Failed to connect to the database.", "error")
    return "Failed to connect to the database."

@users_bp.route('/welcome', methods=['GET', 'POST'])
def welcome():
    error_message = None

    if request.method == 'POST':
        name = request.form.get('name')

        if name:
            if User.is_name_unique(name):
                if User.insert_user(name):
                    flash("User successfully added!", "success")
                    return redirect(url_for('users.temp'))
                else:
                    error_message = "Error occurred while processing the request."
            else:
                error_message = "Name already exists. Please choose a different name."
        else:
            error_message = "Name is required."

    return render_template('welcome.html', error_message=error_message)