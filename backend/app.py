from flask import Flask
from api.auth_routes import auth_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # ✅ 這行會把 MONGO_DB_NAME 放進 app.config
    # 註冊 Blueprint
    app.register_blueprint(auth_bp)

    @app.get("/api/health")
    def api_health():
        return {"status": "ok"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)