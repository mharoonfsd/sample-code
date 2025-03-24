#!/mnt/5C2131BF4C26B6D0/Workspace/projects/PytestFlaskTest/lin-conda-py3venv/bin/python
# Run a test server.
from app import create_app
from app.mod_auth import AUTH_MODULE as auth_module

app = create_app()
app.register_blueprint(auth_module)

app.run(host='0.0.0.0', port=8080, debug=True)