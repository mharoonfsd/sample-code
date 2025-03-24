# Import the database object (DB) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from . import DB

# Define a base model for other database tables to inherit
class Base(DB.Model):

    __abstract__  = True

    id            = DB.Column(DB.Integer, primary_key=True)
    date_created  = DB.Column(DB.DateTime,  default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime,  default=DB.func.current_timestamp(),
                                           onupdate=DB.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name    = DB.Column(DB.String(128),  nullable=False)

    # Identification Data: email & password
    email    = DB.Column(DB.String(128),  nullable=False,
                                            unique=True)
    password = DB.Column(DB.String(192),  nullable=False)

    # Authorisation Data: role & status
    role     = DB.Column(DB.SmallInteger, nullable=False)
    status   = DB.Column(DB.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name     = name
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)