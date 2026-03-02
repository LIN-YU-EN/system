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

    username = data.get("username")
    password = data.get("password")
    class_id = data.get("class_id")
    role = data.get("role", "student")

    if not username or not password or not class_id:
        return {"success": False, "message": "username/password/class_id required"}, 400

    user, err = create_user(username, password, role, class_id)
    if err:
        # 這裡最常見就是 username already exists
        return {"success": False, "message": err}, 409

    # 統一成功格式
    return ok(message="registered", data=user, status_code=201)

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"success": False, "message": "username/password required"}, 400

    user, err = verify_user(username, password)
    if err:
        return {"success": False, "message": err}, 401

    # 統一成功格式
    return ok(message="login ok", data=user, status_code=200)