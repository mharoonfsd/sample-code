#!F:\Workspace\projects\PytestFlaskTest\win-conda-py3venv/win-conda-py3venv/python
# Run a test server.
from app import create_app
from app.mod_auth import AUTH_MODULE as auth_module

app = create_app()
app.register_blueprint(auth_module)

app.run(host='0.0.0.0', port=8080, debug=True)