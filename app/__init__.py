from flask import Flask, render_template
from .database import init_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    init_db(app)

    @app.get("/")
    def index_get():
        return render_template("index.html")

    @app.get("/login")
    def login_get():
        return render_template("login.html")

    return app
