from flask import Blueprint, render_template, request, jsonify, session
from app.services.chatbot_service import ask_chatbot
from app.utils.auth_decorator import login_required

chatbot = Blueprint("chatbot", __name__)

@chatbot.route("/assistant")
@login_required
def assistant():
    if "chat_history" not in session:
        session["chat_history"] = []

    return render_template("chatbot.html")


@chatbot.route("/api/chat", methods=["POST"])
@login_required
def chat():
    message = request.json.get("message")
    history = session.get("chat_history", [])
    reply = ask_chatbot(message, history)
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    session["chat_history"] = history[-10:]

    return jsonify({"reply": reply})