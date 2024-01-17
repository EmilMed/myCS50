from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, Email, DataRequired
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import csv

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes = 5)

app.config.update(dict( DEBUG = True,
    MAIL_SERVER = "smtp-mail.outlook.com",
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = "zceceme@ucl.ac.uk",
    MAIL_PASSWORD = "-@3VWFP.itf+b<?876hru"))

db = SQLAlchemy(app)
mail = Mail(app)

mail.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = users.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one.")
        
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField(validators=[DataRequired(), Email()])
    message = TextAreaField(validators=[DataRequired(), Length(min=3, max=10000)])
    submit = SubmitField()

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        with open("form_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
        return redirect(url_for("home"))
    return render_template("mainpage.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("user"))
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(username=form.username.data).first()  
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You have successfully logged in!")
                return redirect(url_for("user"))
            else:
                flash("Your password is incorrect.")
        else:
            flash("No such user.")
    return render_template('login.html', form=form)


@app.route("/user", methods=["POST", "GET"])
@login_required
def user():
    form = ContactForm()
    if form.validate_on_submit():
        with open("form_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
            flash("Your enquiry has been submitted!")
        return redirect(url_for("user"))
    return render_template("user.html", form=form)

    
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered", "info")
        return redirect(url_for("user"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = users(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("You have successfully created your own account!")
        return redirect("/login")
    flash("Please, insert relevant data.")
    return render_template('register.html', form=form)


@app.route("/subscriptions")
@login_required
def subscribepage():
    form = ContactForm()
    if form.validate_on_submit():
        with open("form_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
            flash("Your enquiry has been submitted!")
        return redirect(url_for("subscriptions"))
    return render_template("subscriptions.html", form=form)

@app.route("/help&support")
def HandS():
    form = ContactForm()
    if form.validate_on_submit():
        with open("form_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
            flash("Your enquiry has been submitted!")
        return redirect(url_for("help&support"))
    return render_template("help&support.html", form=form)

@app.route("/programmes")
def programmes():
    flash("You have purchased your fitness subscription!")
    form = ContactForm()
    if form.validate_on_submit():
        with open("form_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
        return redirect(url_for("home"))
    return render_template("programmes.html", form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
 