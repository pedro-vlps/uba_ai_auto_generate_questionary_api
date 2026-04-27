"""Authentication controller handling login requests and token generation."""

from src.services.auth_service import AuthService
from src.utils.jwt_utils import JWTUtils


class AuthController:
    """Controller for handling authentication-related operations."""

    @staticmethod
    async def login(nickname: str, password: str, db):
        """
        Process user login and generate JWT token.

        Args:
            nickname: User's nickname for authentication
            password: User's password for authentication
            db: Database session for querying user data

        Returns:
            dict: Contains JWT token on success or error message on failure
        """
        try:
            user = await AuthService.login(nickname, password, db)
            token_response = JWTUtils.encode_jwt({"id": str(user.user.id)})

            return {"token": token_response, "user": user}

        except ValueError as e:
            return {"error": str(e)}
