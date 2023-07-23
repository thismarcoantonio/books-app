from flask import Flask, render_template
from .database import init_db
from .routes.auth import bp as auth_bp
from .routes.views import bp as views_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    # Database setup
    init_db(app)

    # Blueprint registrations
    app.register_blueprint(auth_bp)
    app.register_blueprint(views_bp)

    return app
