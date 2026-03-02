from db.mongo import col


def create_user(username: str, password: str, role: str, class_id: str):
    users = col("users")

    # username 必須唯一
    if users.find_one({"username": username}):
        return None, "username already exists"

    doc = {
        "username": username,
        "password": password,   # 暫時用明碼（你說先不要 hash）
        "role": role,
        "class_id": class_id,
    }
    result = users.insert_one(doc)

    data = {
        "id": str(result.inserted_id),
        "username": username,
        "role": role,
        "class_id": class_id,
    }
    return data, None


def verify_user(username: str, password: str):
    users = col("users")
    user = users.find_one({"username": username})
    if not user:
        return None, "user not found"

    if user.get("password") != password:
        return None, "invalid password"

    data = {
        "id": str(user["_id"]),
        "username": user["username"],
        "role": user.get("role"),
        "class_id": user.get("class_id"),
    }
    return data, None