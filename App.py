from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Home'
    return render_template('/pages/home.html', title = title)

@app.route('/about')
def about():
    title = 'About'
    return render_template('/pages/about.html', title = title)

if __name__ == '__main__':
    app.run(debug = True)
