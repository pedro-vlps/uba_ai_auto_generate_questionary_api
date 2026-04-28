from sqlalchemy import select

from src.models import Profiles


class ProfilesService:
    @staticmethod
    async def get_uba_profile(db):
        async with db as session:
            query = select(Profiles).where(Profiles.name == "basic_uba_user")

            result = await session.execute(query)
            profile = result.scalars().first()

            return profile
