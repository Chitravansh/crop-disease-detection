from flask import Blueprint, render_template
from app.utils.auth_decorator import login_required

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/detect")
@login_required
def detect():
    return render_template("detect.html")


@main.route("/diseases")
@login_required
def diseases():
    return render_template("diseases.html")


@main.route("/about")
def about():
    return render_template("about.html")
