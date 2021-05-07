import os
from datetime import timedelta

from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

from classes.Paths import get_database_path
from src.blue_access_management import access_management
from src.blue_auth import auth
from src.blue_change_password import change_password
from src.blue_equipment import equipment
from src.blue_files import files
from src.blue_profile import profile
from src.blue_reset_password import reset_password
from src.blue_suppliers import suppliers
from src.blue_users import users
from classes.Database import Database
from classes.Model import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + get_database_path()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

app.register_blueprint(equipment)
app.register_blueprint(users)
app.register_blueprint(profile)
app.register_blueprint(suppliers)
app.register_blueprint(auth)
app.register_blueprint(change_password)
app.register_blueprint(reset_password)
app.register_blueprint(files)
app.register_blueprint(access_management)

# -------------------------------------------------------------------------------

db1 = Database()
db1.create_db()
db = SQLAlchemy(app)

# -------------------------------------------------------------------------------

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

if not os.path.exists('static/images/upload'):
    os.makedirs('static/images/upload')
if not os.path.exists('static/docs/upload'):
    os.makedirs('static/docs/upload')


@login_manager.user_loader
def load_user(user_id):
    # return User.query.get(int(user_id))
    print(User.query.filter_by(id=user_id))
    return User.query.filter_by(id=user_id).first()


@app.route("/")
def main():
    return redirect(url_for('equipment._equipment'))


@app.route("/test")
def test():
    return '123'


if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
    app.run(host="0.0.0.0", port=5000)
