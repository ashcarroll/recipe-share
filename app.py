from datetime import datetime, timezone

from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import User, Recipe, Favorite, Cuisine, db

app = Flask(__name__)
app.config.from_object('config')

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)