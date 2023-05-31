from flask import Blueprint, render_template

bp = Blueprint("views", __name__)


@bp.get("/")
def index_get():
    return render_template("index.html")


@bp.get("/login")
def login_get():
    return render_template("login.html")
