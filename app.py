from flask import Flask
from controllers.users import users_bp
import secrets


app = Flask(__name__)


#don't forget secret key
app.secret_key = secrets.token_hex(32)




# Register users blueprint
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
