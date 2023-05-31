from flask import Blueprint
from app.database import get_db

bp = Blueprint('auth', __name__)
