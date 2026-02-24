from fastapi import APIRouter
from fastapi import Query
from fastapi import status

from app.core.exceptions import http_errors
from app.core.telemetry import logger

router = APIRouter(tags=["Error-Examples"])


@router.get("/error/bad-request")
async def bad_request_example(message: str = Query(None)):
    """
    Retorna um erro 400 Bad Request.
    Exemplo: /error/bad-request?message=dados%20inválidos
    """
    detail = message or "Requisição inválida. Verifique os parâmetros enviados."
    logger.warning(
        detail,
        extra={
            "exception_type": "BadRequestError",
            "status_code": status.HTTP_400_BAD_REQUEST,
        },
    )
    raise http_errors.bad_request(detail=detail)


@router.get("/error/unauthorized")
async def unauthorized_example(message: str = Query(None)):
    """
    Retorna um erro 401 Unauthorized (credenciais inválidas).
    Exemplo: /error/unauthorized?message=login%20inválido
    """
    detail = message or "Credenciais inválidas. Verifique seu login e senha."
    logger.warning(
        detail,
        extra={
            "exception_type": "InvalidCredentials",
            "status_code": status.HTTP_401_UNAUTHORIZED,
        },
    )
    raise http_errors.invalid_credentials(detail=detail)


@router.get("/error/forbidden")
async def forbidden_example(message: str = Query(None)):
    """
    Retorna um erro 403 Forbidden (erro de autenticação).
    Exemplo: /error/forbidden?message=acesso%20negado
    """
    detail = message or "Acesso negado. Você não tem permissão para acessar este recurso."
    logger.warning(
        detail,
        extra={
            "exception_type": "AuthError",
            "status_code": status.HTTP_403_FORBIDDEN,
        },
    )
    raise http_errors.auth_error(detail=detail)


@router.get("/error/not-found")
async def not_found_example(message: str = Query(None)):
    """
    Retorna um erro 404 Not Found.
    Exemplo: /error/not-found?message=recurso%20não%20encontrado
    """
    detail = message or "Recurso não encontrado."
    logger.warning(
        detail,
        extra={
            "exception_type": "NotFoundError",
            "status_code": status.HTTP_404_NOT_FOUND,
        },
    )
    raise http_errors.not_found(detail=detail)


@router.get("/error/validation")
async def validation_error_example(message: str = Query(None)):
    """
    Retorna um erro 422 Unprocessable Entity (erro de validação).
    Exemplo: /error/validation?message=dados%20inválidos
    """
    detail = message or "Erro de validação. Os dados enviados não são válidos."
    logger.warning(
        detail,
        extra={
            "exception_type": "ValidationError",
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
        },
    )
    raise http_errors.validation_error(detail=detail)


@router.get("/error/conflict")
async def conflict_example(message: str = Query(None)):
    """
    Retorna um erro 409 Conflict (recurso duplicado).
    Exemplo: /error/conflict?message=recurso%20já%20existe
    """
    detail = message or "Recurso já existe. Não é possível criar um duplicado."
    logger.warning(
        detail,
        extra={
            "exception_type": "DuplicatedError",
            "status_code": status.HTTP_409_CONFLICT,
        },
    )
    raise http_errors.duplicated_error(detail=detail)


@router.get("/error/internal-server")
async def internal_server_error_example():
    """
    Retorna um erro 500 Internal Server Error.
    Simula um erro não tratado no servidor.
    """
    # logger.error(
    #     "Erro interno do servidor não tratado",
    #     extra={
    #         "exception_type": "InternalServerError",
    #         "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     },
    # )
    raise Exception("Erro interno do servidor não tratado")
