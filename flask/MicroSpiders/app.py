"""The main application."""

import connexion
from settings import SERVER

app = connexion.App(__name__, **SERVER, specification_dir='swagger/')
