from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import  RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c21f402817d5f58c1e1ac7321371d292'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(20), unique=True, nullable=False)
    email = db.email(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='defualt.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}




posts = [
    {
        'author': 'Nishant',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 10, 2018'
    },
    {
        'author': 'Abhi',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'December 9, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)




