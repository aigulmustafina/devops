import jwt

SECRET = "hello-from-jusan"
PAYLOAD_KEY = "postBody"
PAYLOAD_VALUE = "request from curl"

def validate(payload: str) -> bool:
    if not isinstance(payload, str):
        return False
    key, val = payload.split(":")
    return key == PAYLOAD_KEY and val == PAYLOAD_VALUE

def check(token):
    try:
        body = jwt.decode(token, SECRET, algorithms="HS256")
        return validate(body.get("payload"))
    except Exception:
        return False
