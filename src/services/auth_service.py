"""Authentication service for user validation."""
from sqlalchemy import select

from src.models import Users
from src.utils.fernet_utils import FernetUtils

fernet_utils = FernetUtils()


class AuthService:
    """Service for handling user authentication operations."""

    @staticmethod
    async def login(nickname: str, password: str, db):
        """
        Authenticate a user by nickname and password.

        Args:
            nickname: User's nickname for authentication
            password: User's password for authentication
            db: Database session for querying user data

        Returns:
            Users: User object if authentication succeeds

        Raises:
            ValueError: If nickname or password is invalid
        """
        query = select(Users)

        result = await db.execute(query)
        data = result.scalars().all()

        for user in data:
            if (
                fernet_utils.decrypt(user.nickname) == nickname
                and fernet_utils.decrypt(user.password) == password
            ):
                return user

        raise ValueError("Invalid nickname or password")
