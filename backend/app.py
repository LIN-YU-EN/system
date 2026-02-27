from flask import Flask
from api.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)

    # 註冊 Blueprint
    app.register_blueprint(auth_bp)

    @app.get("/api/health")
    def api_health():
        return {"status": "ok"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)