from flask import Flask
from models.database import db
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()

    swagger_ui_blueprint = get_swaggerui_blueprint(
        "/api/docs",
        "/static/swagger.json"
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix="/api/docs")

    app.run()
