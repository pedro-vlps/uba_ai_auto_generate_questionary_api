from datetime import datetime, timedelta, timezone
import jwt

from src.configs.configs import settings


class JWTUtils:
    @staticmethod
    def decode_jwt(token: str) -> dict:
        """
        Decode a JWT token and return the payload.

        Args:
            token: The JWT token to decode

        Returns:
            dict: The decoded payload

        Raises:
            jwt.ExpiredSignatureError: If the token has expired
            jwt.InvalidTokenError: If the token is invalid
        """
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload

    @staticmethod
    def encode_jwt(payload: dict, expiration_minutes: int | None = None) -> str:
        """
        Encode a payload into a JWT token.

        Args:
            payload: The data to encode in the token
            expiration_minutes: Token expiration time in minutes (default: 30)

        Returns:
            str: The encoded JWT token
        """
        payload_copy = payload.copy()

        exp_minutes = expiration_minutes or settings.EXPIRATION_MINUTES
        expiration = datetime.now(timezone.utc) + timedelta(minutes=exp_minutes)
        payload_copy["exp"] = expiration

        token = jwt.encode(
            payload_copy, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return token
