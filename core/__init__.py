# blog_system/core/__init__.py
from flask import Flask
from .extensions import db, migrate
from .routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('core.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)

    return app
