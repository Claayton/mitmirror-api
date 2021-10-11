def test_encode_auth_token(client):
    from app.models.users import Token

    data = {
        "email": "test@test.com",
        "password": "test123"
    }
    auth_token = Token.encode_jwt(data['email'], data['password'])
    assert auth_token['Authorization'] is not None

def test_decode_auth_token2(client):
    from app.models.users import Token
    auth_token =Token.encode_jwt("test@test.com", "test123")
    decoded_token = Token.decode_jwt(auth_token['Authorization'])

    assert decoded_token.username == 'test123'
