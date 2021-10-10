def test_if_secret_key_is_not_my_precious(config):
    assert config['SECRET_KEY'] is not 'my_precious'

def test_if_debug_is_true(config):
    assert config['DEBUG'] is True

def test_if_current_app_is_not_none(client):
    from flask import current_app
    assert current_app is not None

def test_if_db_is_sqlite3(config):
    assert config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///tests.sqlite3'
