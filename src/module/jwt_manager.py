from datetime import datetime, timedelta

from jose import jwt

from module.constants import JWT_SECRET


class JWTManager:
    @classmethod
    def create_jwt(cls, username: str) -> str:
        """创建JWT"""
        return jwt.encode({
            'username': username,
            'exp': datetime.utcnow() + timedelta(hours=2)
        }, JWT_SECRET, algorithm='HS256')
