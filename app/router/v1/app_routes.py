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
        "IPcountry": headers.get("CF-IPCountry"),
        "IPcity": headers.get("CF-IPCity"),
        "IPcontinent": headers.get("CF-IPContinent"),
        "IPlatitude": headers.get("CF-IPLatitude"),
        "IPlongitude": headers.get("CF-IPLongitude"),
        "IPpostal_code": headers.get("CF-IPPostalCode"),
        "IPtimezone": headers.get("CF-IPTimezone"),
        "asOrganization": headers.get("CF-IPASNOrganization"),  # ISP
        "country": headers.get("country"),
        "city": headers.get("city"),
        "continent": headers.get("continent"),
        "region": headers.get("region"),
        "regionCode": headers.get("regionCode"),
        "timezone": headers.get("timezone"),
        "longitude": float(headers.get("longitude")) if headers.get("CF-IPLongitude") else None,
        "latitude": float(headers.get("latitude")) if headers.get("CF-IPLatitude") else None,
        "postalCode": headers.get("postalCode"),
    }

    return GeoLocation(**geo)
