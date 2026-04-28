"""Request-scoped storage for authentication cookie operations."""
from contextvars import ContextVar


_auth_token_ctx: ContextVar[str | None] = ContextVar("auth_token_ctx", default=None)


class AuthCookieContext:
    """Store auth token data during a request so middleware can persist it safely."""

    @staticmethod
    def set_token(token: str) -> None:
        """Register a token to be written as a secure cookie in the response."""
        _auth_token_ctx.set(token)

    @staticmethod
    def get_token() -> str | None:
        """Read the token scheduled for the response cookie."""
        return _auth_token_ctx.get()

    @staticmethod
    def clear() -> None:
        """Reset any pending auth token for the current request context."""
        _auth_token_ctx.set(None)
