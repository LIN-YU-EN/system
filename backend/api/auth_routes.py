from flask import Blueprint
from core.responses import ok
from db.mongo import get_db
from flask import request
from services.auth_service import create_user, verify_user

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.get("/health")
def health():
    return ok(message="auth is alive")


@auth_bp.get("/health/db")
def db_health():
    """
    只檢查 MongoDB 連線是否正常，不做任何寫入。
    """
    try:
        db = get_db()
        db.command("ping")
        return ok(message="MongoDB connected")
    except Exception as e:
        return {"status": "MongoDB error", "error": str(e)}, 500


@auth_bp.get("/init-db")
def init_db():
    """
    初始化資料庫：插入一筆資料，讓 MongoDB Compass 顯示 my_system。
    注意：這不是分級/評量資料，只是初始化用。
    """
    try:
        db = get_db()

        result = db["users"].insert_one({
            "system": "my_system",
            "status": "initialized"
        })

        return {"message": "DB initialized", "id": str(result.inserted_id)}, 200
    except Exception as e:
        return {"message": "init failed", "error": str(e)}, 500

@auth_bp.post("/register")
def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "student")
    class_id = data.get("class_id")

    if not username or not password or not class_id:
        return {"message": "username/password/class_id required"}, 400

    user_id, err = create_user(username, password, role, class_id)
    if err:
        return {"message": err}, 409

    return {"message": "registered", "user_id": user_id}, 201


@auth_bp.post("/login")
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"message": "username/password required"}, 400

    user = verify_user(username, password)
    if not user:
        return {"message": "invalid credentials"}, 401

    # 先回 user 基本資料（下一步再做 JWT）
    return {"message": "login ok", "user": user}, 200