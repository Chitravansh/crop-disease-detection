from flask import Blueprint, render_template, session
from app.services.expert_service import ExpertService
from app.utils.auth_decorator import login_required

experts_bp = Blueprint("experts", __name__)

@experts_bp.route("/experts")
@login_required
def experts_page():

    user_location = session.get("location")

    local_experts = ExpertService.fetch_local_experts(user_location)
    global_experts = ExpertService.fetch_global_experts()

    return render_template(
        "experts.html",
        local_experts=local_experts,
        global_experts=global_experts
    )