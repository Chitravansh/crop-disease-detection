from app.models.expert_model import ExpertModel

class ExpertService:

    @staticmethod
    def fetch_local_experts(user_location=None):
        return ExpertModel.get_local_experts(user_location)

    @staticmethod
    def fetch_global_experts():
        return ExpertModel.get_global_experts()