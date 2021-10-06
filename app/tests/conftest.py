import pytest
from app import tests_app

@pytest.fixture(scope="module")
def app():
    """Instance of Main flask-app"""
    return tests_app()
