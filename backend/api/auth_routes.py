from flask import Blueprint
from core.responses import ok
from db.mongo import get_db

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