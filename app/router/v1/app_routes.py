from fastapi import APIRouter
from fastapi import Request

router = APIRouter(tags=["Password-Generator"])


@router.get("/health")
async def health():
    return {"status": "alive"}


@router.get("/debug")
async def debug(request: Request):
    return {
        "headers": dict(request.headers),
        "geo": {
            "country": request.headers.get("cf-ipcountry"),
            "city": request.headers.get("cf-ipcity"),
            "isp": request.headers.get("cf-ipasnorganization")
        }
    }
