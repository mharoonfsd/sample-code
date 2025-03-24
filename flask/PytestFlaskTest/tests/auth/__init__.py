import os
import tempfile
import pytest

from app import create_app
from app.mod_auth import auth_module

@pytest.fixture
def client():
    app = create_app()
    app.register_blueprint(auth_module)
    
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    client = app.test_client()

    # with app.app_context():
    #     app.init_db()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
