from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class User(UserMixin, db.Model):
    _tablename_ = 'users'
    user_id = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True)
    is_chef = db.mapped_column(db.Boolean, default=False)

class Recipe(db.Model):
    _tablename_ = 'recipes'
    recipe_id = db.mapped_column(db.Integer, primary_key=True)
    recipe_name = db.mapped_column(db.String(500))
    ingredients = db.mapped_column(db.String(1000))
    method = db.mapped_column(db.String(5000))
    total_time = db.mapped_column(db.Integer)


class Favorite(db.Model):
    _tablename_ = 'favorites'
    favorite_id = db.mapped_column(db.Integer, primary_key=True)
    user_id = ...
    recipe_id = ...

class Cuisine(db.Model):
    _tablename_ = 'cuisines'
    cuisine_id = db.mapped_column(db.Integer, primary_key=True)
    cuisine_name = ...