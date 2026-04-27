from sqlalchemy import select

from src.models import Institutions


class InstitutionsService:
    @staticmethod
    async def get_uba_institution(db):
        async with db as session:
            query = select(Institutions).where(Institutions.name == "UBA")

            result = await session.execute(query)
            institution = result.scalars().first()

            return institution
