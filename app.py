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
    return render_template('index.html', cuisines = Cuisine.query.all())

@app.route('/cuisine/<int:cuisine_id>')
def cuisine_category(cuisine_id):
    cuisine = Cuisine.query.get_or_404(cuisine_id)
    return render_template('cuisine.html', cuisine=cuisine)

@app.route('/recipes')
def recipe_list():
    return render_template('recipe_list.html', recipes = Recipe.query.all())

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        ingredients = request.form['ingredients']
        method = request.form['method']
        time = request.form['time']
        db.session.add(Recipe(recipe_name=recipe_name, ingredients=ingredients, method=method, total_time=time))
        db.session.commit()
        return redirect(recipe_list.html)
    
    return render_template('add_recipe.html')

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_action():
    username = request.form['username']
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
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if not user:
        flash(f"This is not an existing username for this site")
        return redirect(url_for('login_page'))
    
    login_user(user)
    flash(f"Hello {username}!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)