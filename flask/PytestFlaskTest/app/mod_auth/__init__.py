from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()
# Define the blueprint: 'auth', set its url prefix: app.url/auth
AUTH_MODULE = Blueprint('auth', __name__, url_prefix='/auth')