import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from app.core.middleware import otel_setup
from app.core.settings import settings
from app.core.telemetry import logger
from app.router.v1 import routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # logger.setLevel(settings.OTEL_PYTHON_LOG_LEVEL)
    logging.getLogger("opentelemetry").propagate = False
    logger.info(f"{settings.OTEL_SERVICE_NAME} initialization started.")
    yield
    logger.info(f"{settings.OTEL_SERVICE_NAME} shutdown completed.")


app = FastAPI(
    title="Password Generator",
    version="1.0.0",
    description="Password api to generate random pins and passwords with cicd pipe, test hadson",
    contact={
        "name": "GabrielCarvalho",
        "email": "gabrielcarvalho.workk@gmail.com",
        "url": "https://www.linkedin.com/in/gabzsz",
    },
)


@app.middleware("http")
async def otel_setup_middleware(request: Request, call_next):
    return await otel_setup(request, call_next)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Liberar para todos os domínios (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=routers)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=80, reload=True)
