import pytest
from app import NewApp

newapp = NewApp()

@pytest.fixture(scope="module")
def app():
    """Instance of Main flask-app"""
    return newapp.create_app()
