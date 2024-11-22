from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class User(UserMixin, db.Model):
    _tablename_ = 'users'
    user_id = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True)
    is_chef = ...

class Recipe(db.Model):
    _tablename_ = 'recipes'
    title = ...
    ingredients = ...
    method = ...
    total_time = ...


class Favorite(db.Model):
    _tablename_ = 'favorites'
    user_id = ...
    recipe_id = ...

class Cuisine(db.Model):
    _tablename_ = 'cuisines'
    name = ...