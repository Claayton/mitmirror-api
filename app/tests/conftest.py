import pytest
from app import minimal_app

@pytest.fixture(scope="module")
def app():
    """Instance of Main flask-app"""
    return minimal_app()
