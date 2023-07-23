import functools
from flask import g, Blueprint, request, redirect, flash, session, url_for
from peewee import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from ..database.models import Author

bp = Blueprint("auth", __name__)


@bp.post("/login")
def login_post():
    errors = []
    username = request.form["username"]
    password = request.form["password"]

    if not username:
        errors.append("Username is required.")
    if not password:
        errors.append("Password is required.")

    user = Author.get_or_none(name=username)

    if user is None:
        errors.append("Incorrect username")
    elif not check_password_hash(user.password, password):
        errors.append("Incorrect password")

    if not errors:
        session.clear()
        session["user_id"] = user.id
        return redirect(url_for("views.index"))
    for error in errors:
        flash(error)
    return redirect(url_for("views.login"))


@bp.post("/register")
def register_post():
    errors = []
    username = request.form["username"]
    password = request.form["password"]

    if not username:
        errors.append("Username is required.")
    if not password:
        errors.append("Password is required.")

    if not errors:
        try:
            hashed_password = generate_password_hash(password)
            Author.create(name=username, password=hashed_password)
        except IntegrityError:
            errors.append(f"User {username} is already registered.")
        else:
            return redirect(url_for("views.login"))
    for error in errors:
        flash(error)
    return redirect(url_for("views.register"))


@bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("views.index"))


@bp.before_app_request
def load_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = Author.get_by_id(user_id)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("views.login"))

        return view(**kwargs)

    return wrapped_view


def logged_out_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user:
            return redirect(url_for("views.index"))

        return view(**kwargs)

    return wrapped_view
