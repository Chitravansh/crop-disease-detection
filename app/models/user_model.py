from datetime import datetime
from app.database.mongo import users_collection
from app.utils.password_utils import hash_password


def create_user(name, email, password, language="en", location="unknown"):
    user = {
        "name": name,
        "email": email,
        "password": hash_password(password),
        "preferred_language": language,
        "location": location,
        "created_at": datetime.utcnow(),
    }
    users_collection.insert_one(user)
    return user


def find_user_by_email(email):
    return users_collection.find_one({"email": email})
