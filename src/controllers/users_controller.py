"""Controller for Users table"""

from fastapi import HTTPException
from api_crud_generate_libary.services.service import Service

from src.models import Users, UsersInstitutions
from src.services.institutions_service import InstitutionsService
from src.services.profiles_service import ProfilesService
from src.utils.fernet_utils import FernetUtils

fernet = FernetUtils()
generic_user_service = Service(Users)
generic_user_institution_service = Service(UsersInstitutions)


class UsersController:
    """Controller class for handling user-related operations."""

    @staticmethod
    async def create_user(body, db):
        """Create a new user in the database after checking for nickname uniqueness."""
        users = await generic_user_service.read(
            db,
            join_parameters=None,
            second_level_join_parameters=None,
            page=None,
            items_per_page=None,
            order_by=None,
            direction=None,
        )

        for user in users[0]:
            if fernet.decrypt(user.nickname) == fernet.decrypt(body.nickname):
                raise HTTPException(status_code=400, detail="Nickname already exists")

        new_user = await generic_user_service.create(
            body.model_dump(),
            db,
            join_parameters=None,
            second_level_join_parameters=None,
        )

        uba_institution = await InstitutionsService.get_uba_institution(db)
        uba_profile = await ProfilesService.get_uba_profile(db)

        return await generic_user_institution_service.create(
            {
                "user_id": new_user.id,
                "institution_id": uba_institution.id,
                "profile_id": uba_profile.id,
            },
            db,
            join_parameters=None,
            second_level_join_parameters=None,
        )
