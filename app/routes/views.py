from flask import Blueprint, render_template
from .auth import logged_out_required

bp = Blueprint("views", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.get("/login")
@logged_out_required
def login():
    return render_template("login.html")


@bp.get("/register")
@logged_out_required
def register():
    return render_template("register.html")
