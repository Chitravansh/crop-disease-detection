from flask import Blueprint, request, jsonify, session
from app.utils.auth_decorator import login_required
from app.models.user_model import update_user_location
from bson import ObjectId

location_bp = Blueprint("location", __name__)


@location_bp.route("/api/location", methods=["POST"])
@login_required
def set_location():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "No data received"}), 400

        location = {
            "city": data.get("city"),
            "state": data.get("state"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }

        # Store in session
        session["location"] = location

        # Store in DB (persistent)
        user_id = session.get("user")

        if user_id:
            update_user_location(ObjectId(user_id), location)

        return jsonify({"status": "success"})

    except Exception as e:
        print("Location Error:", str(e))
        return jsonify({"status": "error", "message": "Failed to save location"}), 500