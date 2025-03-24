"""Resolvers that resolve the requests to microservice."""

from connexion.resolver import RestyResolver

from . import application


application.add_api('my_super_app.yaml', resolver=RestyResolver('api'))