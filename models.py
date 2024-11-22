from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class User(UserMixin, db.Model):
    _tablename_ = 'users'
    user_id = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True)

class Recipe(db.Model):
    _tablename_ = 'recipes'

class Favorite(db.Model):
    _tablename_ = 'favorites'

class Cuisine(db.Model):
    _tablename_ = 'cuisines'