from .api.auth import auth_bp
from .api.posts import posts_bp


def apply_routes(app):
    # Registrar blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(posts_bp, url_prefix='/posts')
