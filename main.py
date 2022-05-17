from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'


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