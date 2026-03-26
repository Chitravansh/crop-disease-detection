from app.models.expert_model import ExpertModel


class ExpertService:

    @staticmethod
    def get_experts(user_location):

        # Always return consistent structure
        result = {
            "local": [],
            "global": []
        }

        if not user_location:
            result["global"] = ExpertModel.get_global_experts()
            return result

        city = user_location.get("city")
        state = user_location.get("state")

        # City match (highest priority)
        if city:
            local = ExpertModel.get_by_city(city)

            if local:
                result["local"] = local
                result["global"] = ExpertModel.get_global_experts()
                return result

        # State match (fallback)
        if state:
            state_experts = ExpertModel.get_by_state(state)

            if state_experts:
                result["local"] = state_experts
                result["global"] = ExpertModel.get_global_experts()
                return result

        # Final fallback
        result["global"] = ExpertModel.get_global_experts()

        return result