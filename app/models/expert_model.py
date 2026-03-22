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
    def get_local_experts(location=None):

        query = {"type": "local"}

        if location and location != "unknown":
            city = location.get("city")

            if city:
                query["location"] = {
                    "$regex": city,
                    "$options": "i"
                }

        return list(experts_collection.find(query))

    @staticmethod
    def get_global_experts():
        return list(experts_collection.find({"type": "global"}))

    @staticmethod
    def get_expert_by_id(expert_id):
        return experts_collection.find_one({"_id": ObjectId(expert_id)})