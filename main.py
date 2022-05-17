from flask import Flask, render_template
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    title = 'Home'
    return render_template('/pages/home.html', title = title)


@app.route('/about')
def about():
    title = 'About'
    return render_template('/pages/about.html', title = title)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404