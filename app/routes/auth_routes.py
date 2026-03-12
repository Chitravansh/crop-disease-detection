from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.user_model import create_user, find_user_by_email
from app.utils.password_utils import check_password

auth = Blueprint("auth", __name__)

# ---------- REGISTER ----------


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = find_user_by_email(email)

        if user:
            flash("Email already registered", "warn")
            return redirect(url_for("auth.register"))

        create_user(name, email, password)
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ---------- LOGIN ----------


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = find_user_by_email(email)

        if user and check_password(password, user["password"]):
            session["user"] = str(user["_id"])
            session["name"] = user["name"]
            flash("Login successful!", "success")
            return redirect(url_for("main.home"))

        flash("Invalid credentials", "danger")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


# ---------- LOGOUT ----------


@auth.route("/logout")
def logout():
    session.clear()
    flash("Logout Successful", "success")
    return redirect(url_for("auth.login"))
