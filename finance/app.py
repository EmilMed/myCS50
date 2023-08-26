import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        shares = int(request.form.get("shares"))
        symbol = request.form.get("symbol")
        if not shares:
            return apology("Must input number of shares")
        quote = lookup(symbol.upper())
        if quote == None:
            return apology("Invalid Stock")
        if shares < 0:
            return apology("Shares has to be a positive number!")

        total_cost = shares * quote["price"]
        user_id = session["user_id"]
        cash_atm_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = cash_atm_db[0]["cash"]
        if user_cash < total_cost:
            return apology("Not enough money")
        new_cash = user_cash - total_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
        date = datetime.datetime.now()
        db.execute("INSERT INTO cash flow (user_id, symbol, shares, price, date) VALUES (?, ?, ?, ?, ?)", user_id, quote["symbol"], shares, quote["price"], date)
        flash("Successfully purchased!")
        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must input a symbol")
        quote = lookup(symbol.upper())
        if quote == None:
            return apology("Invalid Stock")
        return render_template("quoted.html", name = quote["name"], price = quote["price"], symbol = quote["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username or not password or not confirmation:
            return apology("Fill in all the fields!")
        if password != confirmation:
            return apology("Check your passwords!")
        hash = generate_password_hash(password)
        try:
            user1 = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Already in use")
        session["user_id"] = user1
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")