from flask import Flask, redirect, url_for, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

app.config['SECRET_KEY'] = "priyamane"

@app.route('/')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)