from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True)
    is_chef = db.mapped_column(db.Boolean, default=False)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.mapped_column(db.Integer, primary_key=True)
    recipe_name = db.mapped_column(db.String(500))
    ingredients = db.mapped_column(db.String(1000))
    method = db.mapped_column(db.String(5000))
    total_time = db.mapped_column(db.Integer)
    date_added = db.mapped_column(db.DateTime, default=datetime.utcnow)
    chef_id = db.mapped_column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    cuisine_id = db.mapped_column(db.Integer, db.ForeignKey('cuisines.cuisine_id'), nullable=False)


class Favorite(db.Model):
    __tablename__ = 'favorites'
    favorite_id = db.mapped_column(db.Integer, primary_key=True)
    user_id = db.mapped_column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipe_id = db.mapped_column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)


class Cuisine(db.Model):
    __tablename__ = 'cuisines'
    cuisine_id = db.mapped_column(db.Integer, primary_key=True)
    cuisine_name = db.mapped_column(db.String(50))