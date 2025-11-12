from fastapi import APIRouter
from fastapi import Request

router = APIRouter(tags=["Password-Generator"])


@router.get("/health")
async def health():
    return {"status": "alive"}


@router.get("/debug")
async def debug(request: Request):
    headers = request.headers
    return {
        "country": headers.get("CF-IPCountry"),
        "city": headers.get("CF-IPCity"),
        "continent": headers.get("CF-IPContinent"),
        "latitude": headers.get("CF-IPLatitude"),
        "longitude": headers.get("CF-IPLongitude"),
        "postal_code": headers.get("CF-IPPostalCode"),
        "timezone": headers.get("CF-IPTimezone")
    }
