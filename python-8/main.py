import jwt


def create_token(data, secret):
    token = jwt.encode(data, secret, algorithm='HS256')
    return token


def verify_signature(token):
    try:
        data = jwt.decode(token, 'acelera', algorithms=['HS256'])
    except jwt.InvalidSignatureError:
        return {"error": 2}
    return data
