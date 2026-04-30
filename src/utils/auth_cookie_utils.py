"""Utilities for reading and writing authentication cookies."""
from fastapi import Request, Response

from src.configs.configs import settings


class AuthCookieUtils:
    """Helpers for extracting and persisting authentication tokens."""

    @staticmethod
    def extract_token(request: Request) -> str | None:
        """Read the token from the Authorization header or auth cookie."""
        authorization = request.headers.get("authorization")
        if authorization:
            scheme, _, token = authorization.partition(" ")
            if scheme.lower() == "bearer" and token:
                return token

        return request.cookies.get(settings.AUTH_COOKIE_NAME)

    @staticmethod
    def set_auth_cookie(response: Response, token: str) -> None:
        """Attach the authentication cookie to the outgoing response."""
        from datetime import datetime, timezone, timedelta
        
        # Safari/iOS requer expires como datetime absoluto, não segundos relativos
        # Isso é compatível com todos os navegadores modernos
        expires_datetime = datetime.now(timezone.utc) + timedelta(seconds=settings.jwt_expiration_seconds)
        
        # Safari/iOS requer Secure=True com SameSite=None para cookies cross-origin
        # Mas também precisa de expires como datetime, não como integer
        response.set_cookie(
            key=settings.AUTH_COOKIE_NAME,
            value=token,
            max_age=settings.jwt_expiration_seconds,
            expires=expires_datetime,
            httponly=True,
            secure=settings.AUTH_COOKIE_SECURE,
            samesite=settings.AUTH_COOKIE_SAMESITE,
            domain=settings.AUTH_COOKIE_DOMAIN,
            path=settings.AUTH_COOKIE_PATH,
        )

    @staticmethod
    def clear_auth_cookie(response: Response) -> None:
        """Delete the authentication cookie from the outgoing response."""
        response.delete_cookie(
            key=settings.AUTH_COOKIE_NAME,
            domain=settings.AUTH_COOKIE_DOMAIN,
            path=settings.AUTH_COOKIE_PATH,
            secure=settings.AUTH_COOKIE_SECURE,
            samesite=settings.AUTH_COOKIE_SAMESITE,
        )
