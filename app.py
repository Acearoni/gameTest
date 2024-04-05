# app.py

from flask import Flask, render_template, redirect, url_for, request
from config import database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            connection = database.connect_to_database()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO users (name) VALUES (%s);", (name,))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return redirect(url_for('welcome'))
                except Exception as e:
                    print("Error executing SQL query:", e)
                    connection.rollback()
                    cursor.close()
                    connection.close()
                    return "Error occurred while processing the request."
            else:
                return "Failed to connect to the database."
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    connection = database.connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name FROM users;")
            users = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template('welcome.html', users=users)
        except Exception as e:
            print("Error executing SQL query:", e)
            connection.rollback()
            cursor.close()
            connection.close()
            return "Error occurred while processing the request."
    else:
        return "Failed to connect to the database."

if __name__ == '__main__':
    app.run(debug=True)
