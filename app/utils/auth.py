import jwt
from datetime import datetime, timedelta
from config import Config

def generate_token(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

def decode_token(token):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
