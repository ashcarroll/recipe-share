from datetime import datetime, timezone

from flask import Flask, render_template, request, redirect, url_for, flash
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
    recipes = Recipe.query.all()
    cuisines = Cuisine.query.all()
    recipe_urls = [url_for('recipe', recipe_id=recipe.recipe_id) for recipe in recipes]
    return render_template('index.html', recipes=recipes, cuisines=cuisines, recipe_urls=recipe_urls)

@app.route('/cuisine/<int:cuisine_id>')
def cuisine_category(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    return render_template('cuisine.html', cuisine=cuisine)

@app.route('/recipes')
def recipe_list():
    return render_template('recipe_list.html', recipes = Recipe.query.all())#

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        cuisine = Cuisine.query.get_or_404(request.form['cuisine_id'])
        db.session.add(Recipe(
            recipe_name=request.form['recipe_name'],
            ingredients=request.form['ingredients'],
            total_time = request.form['time'],
            method = request.form['method'],
            cuisine=cuisine,
            chef=current_user
        ))
        db.session.commit()
        return redirect(url_for('recipe_list'))
    
    else:
        cuisines = Cuisine.query.all()
        return render_template('add_recipe.html', cuisines=cuisines)
    

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_action():
    username = request.form['username'].lower()

    if User.query.filter_by(username=username).first():
        flash(f"This username '{username}' is already taken, try another one")
        return redirect(url_for('register_page'))
    
    is_chef = request.form.get('is_chef').lower() == 'on'
    user = User(username=username, is_chef=is_chef)

    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for('index'))

@app.route('/logout', methods=['GET'])
@login_required
def logout_page():
    return render_template('logout.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout_action():
    logout_user()
    flash("See you next time!")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_action():
    username = request.form['username'].lower()
    user = User.query.filter_by(username=username).first()
    if not user:
        flash(f"This is not an existing username for this site")
        return redirect(url_for('login_page'))
    
    login_user(user)
    flash(f"Hello {username}!")
    return redirect(url_for('index'))

@app.route('/favorites')
@login_required
def favorites():
    favorites = current_user.favorites
    recipes = [favorite.recipe for favorite in favorites]
    return render_template('favorites.html', recipes=recipes)

@app.route('/favorite/<int:recipe_id>', methods=['POST'])
@login_required
def favorite_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    existing_favorite = Favorite.query.filter_by(user_id=current_user.user_id, recipe_id=recipe_id).first()
    if existing_favorite:
        flash(f"You have already favorited {recipe.recipe_name}")

    else:
        favorite = Favorite(user=current_user, recipe=recipe)
        db.session.add(favorite)
        db.session.commit()
        flash(f"You have favorited {recipe.recipe_name}")
    return redirect(url_for('recipe', recipe_id=recipe_id))


if __name__ == '__main__':
    app.run(debug=True)