from datetime import datetime
from datetime import timezone

import httpx
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.telemetry import logger

router = APIRouter(tags=["Password-Generator"])


@router.get("/health")
async def health():
    logger.info("Service is healthy and running.")
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/debug")
async def debug(request: Request):
    logger.info(f"Request headers: {request.headers}")
    return JSONResponse(
        content={
            "headers": dict(request.headers),
            "geo": {
                "country": request.headers.get("cf-ipcountry"),
                "city": request.headers.get("cf-ipcity"),
                "isp": request.headers.get("cf-ipasnorganization"),
            },
        },
        media_type="application/json; charset=utf-8",
    )


@router.get("/password")
async def get_password():
    logger.info("Password fetch triggered")

    url = "https://password.gabrielcarvalho.dev/v1/"
    params = {
        "password_length": 12,
        "quantity": 1,
        "has_punctuation": "true",
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()

        password = data["data"][0]

        return {
            "status": "ok",
            "password": password,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    except httpx.HTTPError as e:
        logger.error(f"Error fetching password: {str(e)}")
        # raise HTTPException(status_code=502, detail="Failed to fetch external password")
