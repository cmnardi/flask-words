# from main import app as flask_app
from main import create_app
import pytest


@pytest.fixture
def app():
    flask_app = create_app()
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
