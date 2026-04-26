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
    def encode_jwt(payload: dict) -> str:
        """
        Encode a payload into a JWT token.

        Args:
            payload: The data to encode in the token

        Returns:
            str: The encoded JWT token
        """

        token = jwt.encode(
            payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return token
