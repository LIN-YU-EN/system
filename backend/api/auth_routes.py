from flask import Blueprint
from core.responses import ok

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.get("/health")
def health():
    return ok(message="auth is alive")