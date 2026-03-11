from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/detect")
def detect():
    return render_template("detect.html")


@main.route("/diseases")
def diseases():
    return render_template("diseases.html")


@main.route("/about")
def about():
    return render_template("about.html")
