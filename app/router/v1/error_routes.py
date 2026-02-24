from fastapi import APIRouter
from fastapi import Query

from app.core.exceptions import http_errors

router = APIRouter(tags=["Error-Examples"])


@router.get("/error/bad-request")
async def bad_request_example(message: str = Query(None)):
    """
    Retorna um erro 400 Bad Request.
    Exemplo: /error/bad-request?message=dados%20inválidos
    """
    raise http_errors.bad_request(
        detail=message or "Requisição inválida. Verifique os parâmetros enviados."
    )


@router.get("/error/unauthorized")
async def unauthorized_example(message: str = Query(None)):
    """
    Retorna um erro 401 Unauthorized (credenciais inválidas).
    Exemplo: /error/unauthorized?message=login%20inválido
    """
    raise http_errors.invalid_credentials(
        detail=message or "Credenciais inválidas. Verifique seu login e senha."
    )


@router.get("/error/forbidden")
async def forbidden_example(message: str = Query(None)):
    """
    Retorna um erro 403 Forbidden (erro de autenticação).
    Exemplo: /error/forbidden?message=acesso%20negado
    """
    raise http_errors.auth_error(
        detail=message or "Acesso negado. Você não tem permissão para acessar este recurso."
    )


@router.get("/error/not-found")
async def not_found_example(message: str = Query(None)):
    """
    Retorna um erro 404 Not Found.
    Exemplo: /error/not-found?message=recurso%20não%20encontrado
    """
    raise http_errors.not_found(
        detail=message or "Recurso não encontrado."
    )


@router.get("/error/validation")
async def validation_error_example(message: str = Query(None)):
    """
    Retorna um erro 422 Unprocessable Entity (erro de validação).
    Exemplo: /error/validation?message=dados%20inválidos
    """
    raise http_errors.validation_error(
        detail=message or "Erro de validação. Os dados enviados não são válidos."
    )


@router.get("/error/conflict")
async def conflict_example(message: str = Query(None)):
    """
    Retorna um erro 409 Conflict (recurso duplicado).
    Exemplo: /error/conflict?message=recurso%20já%20existe
    """
    raise http_errors.duplicated_error(
        detail=message or "Recurso já existe. Não é possível criar um duplicado."
    )


@router.get("/error/internal-server")
async def internal_server_error_example():
    """
    Retorna um erro 500 Internal Server Error.
    Simula um erro não tratado no servidor.
    """
    raise Exception("Erro interno do servidor não tratado")
