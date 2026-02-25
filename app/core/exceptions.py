from typing import Any
from typing import Dict
from typing import Optional

from fastapi import HTTPException
from fastapi import status

from app.core.telemetry import logger


class AppExceptions:
    def bad_request(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, str]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "BadRequestError"}
        if extra:
            log_extra.update(extra)
        logger.warning(detail, extra=log_extra)
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail, headers)

    def auth_error(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, str]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "AuthError"}
        if extra:
            log_extra.update(extra)
        logger.warning(detail, extra=log_extra)
        return HTTPException(status.HTTP_403_FORBIDDEN, detail, headers)

    def not_found(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, str]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "NotFoundError"}
        if extra:
            log_extra.update(extra)
        logger.warning(detail, extra=log_extra)
        return HTTPException(status.HTTP_404_NOT_FOUND, detail, headers)

    def validation_error(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "ValidationError"}
        if extra:
            log_extra.update(extra)
        logger.warning(
            detail,
            extra=log_extra,
        )
        return HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail,
            headers,
        )

    def duplicated_error(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "DuplicatedError"}
        if extra:
            log_extra.update(extra)
        logger.warning(
            detail,
            extra=log_extra,
        )
        return HTTPException(status.HTTP_409_CONFLICT, detail, headers)

    def invalid_credentials(
        self,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
        extra: Optional[Dict[str, Any]] = None,
    ) -> HTTPException:
        log_extra = {"exception_type": "InvalidCredentials"}
        if extra:
            log_extra.update(extra)
        logger.warning(
            detail,
            extra=log_extra,
        )
        return HTTPException(status.HTTP_401_UNAUTHORIZED, detail, headers)


http_errors = AppExceptions()
