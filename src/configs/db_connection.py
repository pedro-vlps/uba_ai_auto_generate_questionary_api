"""Database connection setup using SQLAlchemy's asynchronous engine and session maker."""
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.configs.configs import settings
# from src.middlewares.db_audit_logs import set_current_user_id

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)

async_session = async_sessionmaker( # type: ignore[call-overload]
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Provide a database session for dependency injection."""
    session: AsyncSession = async_session()

    # token = request.headers.get("Authorization")
    # user_id = decode_token(token)  if token else None

    # await set_current_user_id(session, user_id)

    try:
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
