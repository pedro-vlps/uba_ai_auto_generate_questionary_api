from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from src.utils.jwt_utils import JWTUtils
from src.utils.constraints import BYPASS_ROUTES


async def jwt_checker(request: Request, call_next):
    """
    Middleware to validate JWT tokens for protected routes.

    Args:
        request: The incoming HTTP request
        call_next: The next middleware or route handler in the chain

    Returns:
        Response: Either an error response if token is invalid, or the next handler's response
    """
    if request.method == "OPTIONS":
        return await call_next(request)

    request_token = request.headers.get("authorization")

    if not request_token and not request.url.path in BYPASS_ROUTES:
        return JSONResponse(status_code=401, content={"detail": "Token is required"})

    token = None
    if request_token:
        _string, token = request_token.split(" ")

    if (
        not request.url.path in BYPASS_ROUTES
        and token
    ):
        try:
            JWTUtils.decode_jwt(token)
        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    response = await call_next(request)
    return response
