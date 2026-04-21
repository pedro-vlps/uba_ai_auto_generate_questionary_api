"""Main API File"""
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from api_crud_generate_libary.routers.router import SqlRouter

from src.routers import ai_anatomy_router, auth_router
from src.models import routes_declaration
from src.middleware.jwt_middleware import jwt_checker

security = HTTPBearer(auto_error=False)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(jwt_checker)

@app.get("/healthy")
def healthy():
    """Healthy check route"""
    return { "status": "Ok" }

app.include_router(
    auth_router,
    prefix="",
    tags=["Authentication"],
)

for route in routes_declaration:
    item = SqlRouter(
        model_class=route["model_class"],
        standard_schema=route["standard_schema"],
        db_session=route["db_session"],
        request_post_schema=route["request_post_schema"],
        request_patch_schema=route["request_update_schema"],
        response_get_schema=route["response_get_schema"],
        response_get_by_id_schema=route["response_get_by_id_schema"],
        response_post_schema=route["response_post_schema"],
        response_delete_schema=route["response_delete_schema"],
        response_patch_schema=route["response_patch_schema"],
        use_get=route["enable_get"],
        use_get_by_id=route["enable_get_by_id"],
        use_post=route["enable_post"],
        use_delete=route["enable_delete"],
        use_patch=route["enable_patch"],
        auth_callback=security,
        join_parameters=route["join_parameters"],
        second_level_join_parameters=route["second_level_join_parameters"],
    )

    app.include_router(
        item.router, prefix=route["route_prefix"], tags=route["route_tags"]
    )

app.include_router(
    ai_anatomy_router,
    prefix="/anatomy",
    tags=["Anatomy"],
    dependencies=[Depends(security)]
)
