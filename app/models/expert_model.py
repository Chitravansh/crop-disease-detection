from bson import ObjectId
from app.database.mongo import db

experts_collection = db["experts"]


class ExpertModel:

    @staticmethod
    def create_expert(data):
        return experts_collection.insert_one(data)

    @staticmethod
    def get_all_experts():
        return list(experts_collection.find())

    @staticmethod
    def get_by_city(city):
        return list(
            experts_collection.find({
                "city": {"$regex": f"^{city}$", "$options": "i"}
            })
        )

    @staticmethod
    def get_by_state(state):
        return list(
            experts_collection.find({
                "state": {"$regex": f"^{state}$", "$options": "i"}
            })
        )

    @staticmethod
    def get_global_experts():
        return list(experts_collection.find({"type": "global"}))

    @staticmethod
    def get_expert_by_id(expert_id):
        return experts_collection.find_one({"_id": ObjectId(expert_id)})