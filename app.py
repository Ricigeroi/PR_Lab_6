from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from models.database import get_db_connection

def create_app():
    app = Flask(__name__)
    return app


if __name__ == "__main__":
    app = create_app()
    import routes

    swagger_ui_blueprint = get_swaggerui_blueprint(
        "/api/docs",
        "/static/swagger.json"
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix="/api/docs")

    app.run()

