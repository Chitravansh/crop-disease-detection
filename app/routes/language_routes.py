from flask import Blueprint, session, redirect, request

language = Blueprint("language", __name__)

@language.route("/set-language/<lang>")
def set_language(lang):
    session["language"] = lang
    return redirect(request.referrer or "/")