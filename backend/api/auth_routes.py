# backend/api/auth_routes.py
from flask import Blueprint, request
from core.responses import ok, fail
from db.mongo import get_db
from services.auth_service import create_user, verify_user

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.get("/health")
def health():
    return ok(message="auth is alive")

@auth_bp.get("/health/db")
def db_health():
    try:
        db = get_db()
        db.command("ping")
        return ok(message="MongoDB 已連接")
    except Exception as e:
        return fail(message="MongoDB error", error=str(e)), 500


@auth_bp.get("/init-db")
def init_db():
    """
    只是用來讓 Compass 看得到 users collection（插入一筆初始化資料）
    """
    try:
        db = get_db()
        result = db["users"].insert_one({
            "system": "my_system",
            "status": "initialized"
        })
        return ok(message="DB initialized", data={"id": str(result.inserted_id)})
    except Exception as e:
        return fail(message="init-db failed", error=str(e)), 500


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    gender = data.get("gender")
    username = data.get("username")
    password = data.get("password")
    class_id = data.get("class_id")
    role = data.get("role", "student")

    if not username or not password or not class_id or not name or not gender:
        return {"success": False, "message": "username/password/name/gender/class_id required"}, 400

    user, err = create_user(username, password, role, class_id, name, gender)
    if err:
        return {"success": False, "message": err}, 409

    return ok(message="registered", data=user, status_code=201)


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"success": False, "message": "username/password required"}, 400

    db = get_db()
    users = db["users"]
    user = users.find_one({"username": username})

    if not user or user.get("password") != password:
        return {"success": False, "message": "invalid credentials"}, 401

    result = {
        "id": str(user["_id"]),
        "username": user["username"],
        "name": user.get("name"),
        "role": user.get("role"),
        "class_id": user.get("class_id"),
    }

    return {"success": True, "user": result}