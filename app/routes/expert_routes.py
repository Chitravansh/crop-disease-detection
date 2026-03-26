from flask import Blueprint, render_template, session
from app.services.expert_service import ExpertService
from app.utils.auth_decorator import login_required

experts_bp = Blueprint("experts", __name__)

@experts_bp.route("/experts")
@login_required
def experts_page():

    location = session.get("location")
    experts = ExpertService.get_experts(location)

    return render_template(
        "experts.html",
        local_experts=experts["local"],
        global_experts=experts["global"],
        city=location.get("city") if location else "Unknown"
    )