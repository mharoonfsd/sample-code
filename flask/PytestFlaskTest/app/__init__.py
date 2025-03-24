# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import config

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module


# Next line shouldn't be here
from app.mod_auth.controllers import AUTH_MODULE

def create_app():
    # Define the WSGI application object
    app = Flask(__name__)

    # Configurations
    app.config.from_object(config)

    # Define the database object which is imported
    # by modules and controllers`
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()

    db = SQLAlchemy(app)
    db.init_app(app)
    # Build the database:
    # This will create the database file using SQLAlchemy
    db.create_all()



    # Simple HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404


    # Register blueprint(s)
    # app.register_blueprint(AUTH_MODULE)
    # app.register_blueprint(xyz_module)
    # ..

    return app
