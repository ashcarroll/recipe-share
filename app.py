from datetime import datetime, timezone

from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import User, Recipe, Favorite, Cuisine, db

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
login_manager.login_view = "login_page"

with app.app_context():
    db.init_app(app)
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html', cuisines=Cuisine.query.all())

if __name__ == '__main__':
    app.run(debug=True)