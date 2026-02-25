from fastapi import APIRouter
from fastapi import Query
from fastapi import Request
from fastapi import status

from app.core.exceptions import http_errors
from app.core.telemetry import logger

router = APIRouter(tags=["errors"])


@router.get("/error/bad-request")
async def bad_request_example(
    request: Request,
    message: str = Query("BadRequestError: Requisição inválida. Verifique os parâmetros enviados."),
):
    """
    Retorna um erro 400 Bad Request.
    Exemplo: /error/bad-request?message=BadRequestError:%20dados%20inválidos
    """
    raise http_errors.bad_request(
        detail=message,
        extra={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "url": str(request.url),
        },
    )


@router.get("/error/unauthorized")
async def unauthorized_example(
    request: Request,
    message: str = Query("InvalidCredentials: Credenciais inválidas. Verifique seu login e senha."),
):
    """
    Retorna um erro 401 Unauthorized (credenciais inválidas).
    Exemplo: /error/unauthorized?message=InvalidCredentials:%20login%20inválido
    """
    raise http_errors.invalid_credentials(
        detail=message,
        extra={
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "url": str(request.url),
        },
    )


@router.get("/error/forbidden")
async def forbidden_example(
    request: Request,
    message: str = Query("AuthError: Acesso negado. Você não tem permissão para acessar este recurso."),
):
    """
    Retorna um erro 403 Forbidden (erro de autenticação).
    Exemplo: /error/forbidden?message=AuthError:%20acesso%20negado
    """
    raise http_errors.auth_error(
        detail=message,
        extra={
            "status_code": status.HTTP_403_FORBIDDEN,
            "url": str(request.url),
        },
    )


@router.get("/error/not-found")
async def not_found_example(
    request: Request,
    message: str = Query("NotFoundError: Recurso não encontrado."),
):
    """
    Retorna um erro 404 Not Found.
    Exemplo: /error/not-found?message=NotFoundError:%20recurso%20não%20encontrado
    """
    raise http_errors.not_found(
        detail=message,
        extra={
            "status_code": status.HTTP_404_NOT_FOUND,
            "url": str(request.url),
        },
    )


@router.get("/error/validation")
async def validation_error_example(
    request: Request,
    message: str = Query("ValidationError: Erro de validação. Os dados enviados não são válidos."),
):
    """
    Retorna um erro 422 Unprocessable Entity (erro de validação).
    Exemplo: /error/validation?message=ValidationError:%20dados%20inválidos
    """
    raise http_errors.validation_error(
        detail=message,
        extra={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "url": str(request.url),
        },
    )


@router.get("/error/conflict")
async def conflict_example(
    request: Request,
    message: str = Query("DuplicatedError: Recurso já existe. Não é possível criar um duplicado."),
):
    """
    Retorna um erro 409 Conflict (recurso duplicado).
    Exemplo: /error/conflict?message=DuplicatedError:%20recurso%20já%20existe
    """
    raise http_errors.duplicated_error(
        detail=message,
        extra={
            "status_code": status.HTTP_409_CONFLICT,
            "url": str(request.url),
        },
    )


@router.get("/error/internal-server")
async def internal_server_error_example(request: Request):
    """
    Retorna um erro 500 Internal Server Error.
    Simula um erro não tratado no servidor.
    """
    logger.error(
        "Erro interno do servidor não tratado",
        extra={
            "exception_type": "InternalServerError",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "url": str(request.url),
        },
    )
    raise Exception("Erro interno do servidor não tratado")
