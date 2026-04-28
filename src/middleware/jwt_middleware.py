import jwt

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from src.utils.auth_cookie_utils import AuthCookieUtils
from src.utils.jwt_utils import JWTUtils
from src.utils.constraints import should_bypass_auth
from src.configs.db_connection import async_session
from src.middleware.check_permissions import check_permissions


def _finalize_auth_response(
    request: Request, response, should_clear_cookie: bool = False
):
    """Persist or clear the auth cookie on the outgoing response."""
    token = getattr(request.state, "auth_token", None)
    if token:
        AuthCookieUtils.set_auth_cookie(response, token)

    if should_clear_cookie:
        AuthCookieUtils.clear_auth_cookie(response)

    return response


async def jwt_checker(request: Request, call_next):
    """
    Middleware to validate JWT tokens for protected routes.

    Args:
        request: The incoming HTTP request
        call_next: The next middleware or route handler in the chain

    Returns:
        Response: Either an error response if token is invalid, or the next handler's response
    """
    request.state.auth_token = None
    bypass_auth = request.method == "OPTIONS" or should_bypass_auth(
        request.method, request.url.path
    )

    if bypass_auth:
        response = await call_next(request)
        return _finalize_auth_response(request, response)

    token = AuthCookieUtils.extract_token(request)
    if not token:
        response = JSONResponse(status_code=401, content={"detail": "Token is required"})
        return _finalize_auth_response(request, response, should_clear_cookie=True)

    try:
        decoded_token = JWTUtils.decode_jwt(token)
        await check_permissions(
            request.headers.get("x-institution-id"),
            decoded_token["id"],
            request.method,
            request.url.path,
            async_session(),
        )

    except jwt.ExpiredSignatureError:
        response = JSONResponse(status_code=401, content={"detail": "Token expired"})
        return _finalize_auth_response(request, response, should_clear_cookie=True)
    except (jwt.InvalidTokenError, HTTPException) as e:
        status_code = getattr(e, "status_code", 401)
        detail = getattr(e, "detail", "Invalid token")
        response = JSONResponse(status_code=status_code, content={"detail": detail})
        return _finalize_auth_response(request, response, should_clear_cookie=True)

    response = await call_next(request)
    return _finalize_auth_response(request, response)
