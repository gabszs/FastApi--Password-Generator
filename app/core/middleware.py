import os
from fastapi import Request
from datetime import datetime
from opentelemetry.trace import get_current_span
from ua_parser import parse as parse_ua


async def otel_setup(request: Request, call_next) -> None:
    span = get_current_span()
    start_time = datetime.now()
    trace_id = span.get_span_context().trace_id
    request.state.trace_id = trace_id

    client_address = request.headers.get("cf-connecting-ip")
    user_agent_str = request.headers.get("user-agent")

    ua = parse_ua(user_agent_str) if user_agent_str else None
    sec_ch_ua_platform = request.headers.get("sec-ch-ua-platform")

    # Extrai o body se existir
    request_body = None
    try:
        request_body = await request.json()
    except Exception:
        pass

    event: dict = {
        # Service attributes
        "service.environment": os.getenv("ENVIRONMENT", "development"),
        "deployment.environment": os.getenv("ENVIRONMENT", "development"),
        "service.team": "gabrielcarvalho",
        "service.owner": "gabrielcarvalho",
        "service.version": os.getenv("SERVICE_VERSION"),
        "service.discord": "kali9849",
        "service.build.git_hash": os.getenv("COMMIT_HASH"),
        "service.build.git_branch": os.getenv("COMMIT_BRANCH"),
        "service.build.deployment.user": os.getenv("DEPLOYMENT_USER"),
        "service.build.deployment.trigger": os.getenv("DEPLOYMENT_TRIGGER"),
        # Client geo attributes (from Cloudflare headers)
        "client.geo.country.iso_code": request.headers.get("cf-ipcountry"),
        "client.geo.locality.name": request.headers.get("cf-ipcity"),
        "client.geo.location.lat": request.headers.get("cf-iplatitude"),
        "client.geo.location.lon": request.headers.get("cf-iplongitude"),
        "client.geo.region.iso_code": request.headers.get("cf-region-code"),
        "client.geo.postal_code": request.headers.get("cf-postal-code"),
        "client.geo.continent.code": request.headers.get("cf-ipcontinent"),
        "cloud.availability_zone": request.headers.get("cf-ray", "").split("-")[-1] if request.headers.get("cf-ray") else None,
        # User agent attributes
        "user_agent.original": user_agent_str,
        "user_agent.device.model": ua.device.model if ua and ua.device else None,
        "user_agent.device.type": ua.device.family if ua and ua.device else None,
        "user_agent.device.vendor": ua.device.brand if ua and ua.device else None,
        "user_agent.os": ua.os.family if ua and ua.os else None,
        "user_agent.os.version": f"{ua.os.major}.{ua.os.minor}" if ua and ua.os and ua.os.major else None,
        "user_agent.browser": ua.user_agent.family if ua and ua.user_agent else None,
        "user_agent.browser_version": f"{ua.user_agent.major}.{ua.user_agent.minor}" if ua and ua.user_agent and ua.user_agent.major else None,
        # Browser attributes (Client Hints)
        "browser.brands": request.headers.get("sec-ch-ua"),
        "browser.mobile": request.headers.get("sec-ch-ua-mobile") == "?1",
        "browser.platform": sec_ch_ua_platform.replace('"', '') if sec_ch_ua_platform else None,
        # Request attributes
        "http.request.id": request.headers.get("cf-ray"),
        "client.address": client_address,
        **({"http.request.body": request_body} if request_body is not None else {}),
    }

    request.state.wide_event = event

    response = await call_next(request)

    status_code = response.status_code
    is_error = status_code >= 400
    is_rate_limit = status_code == 429

    event["http.response.status_code"] = status_code
    event["duration_ms"] = (datetime.now() - start_time).total_seconds() * 1000
    event["ratelimit.triggered"] = is_rate_limit
    event["outcome"] = "error" if is_error else "success"

    response.headers["x-trace-id"] = format(trace_id, "032x")