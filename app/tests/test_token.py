def test_encode_auth_token(client):
    from app.models.users import Token

    data = {
        "email": "test@test.com",
        "password": "test123"
    }
    auth_token = Token.encode_jwt(data['email'], data['password'])
    assert auth_token[1] == 200

def test_decode_auth_token2(client):
    from app.models.users import Token

    data = {
        "email": "test@test.com",
        "password": "test123"
    }
    auth_token = Token.encode_jwt(data['email'], data['password'])
    token = auth_token[2]['Authorization']
    assert Token.decode_jwt(token).username == 'test123'
