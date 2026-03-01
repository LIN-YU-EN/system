from werkzeug.security import generate_password_hash, check_password_hash
from db.mongo import col

def create_user(username: str, password: str, role: str, class_id: str):
    users = col("users")

    # username 必須唯一
    if users.find_one({"username": username}):
        return None, "username already exists"

    doc = {
        "username": username,
        "password_hash": generate_password_hash(password),
        "role": role,
        "class_id": class_id,
    }
    result = users.insert_one(doc)
    return str(result.inserted_id), None

def verify_user(username: str, password: str):
    users = col("users")
    user = users.find_one({"username": username})
    if not user:
        return None

    if not check_password_hash(user["password_hash"], password):
        return None

    # 回傳必要資訊（不要回傳 password_hash）
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "role": user.get("role"),
        "class_id": user.get("class_id"),
    }