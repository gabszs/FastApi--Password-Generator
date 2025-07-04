from fastapi import APIRouter

from .app_routes import router as app_router
from .password_routes import router

routers = APIRouter(prefix="/v1")
routers.include_router(router)
routers.include_router(app_router)

__all__ = ["routers"]
