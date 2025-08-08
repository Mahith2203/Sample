from datetime import datetime, timedelta
from jose import jwt
from src.config import settings

# NOTE: This scaffold uses an in-memory user store for simplicity
USERS = {"demo@example.com": {"password": "demo"}}

async def login(payload: dict):
    email = payload.get('email')
    password = payload.get('password')
    user = USERS.get(email)
    if not user or user.get('password') != password:
        return {"error": "invalid_credentials"}

    expire = datetime.utcnow() + timedelta(minutes=1440)
    token = jwt.encode({"sub": email, "exp": expire.timestamp()}, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return {"access_token": token, "token_type": "bearer"}

async def register(payload: dict):
    # For demo only — replace with real DB logic
    email = payload.get('email')
    USERS[email] = {"password": payload.get('password')}
    return {"status": "ok"}