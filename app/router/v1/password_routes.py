from asyncio import gather
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from app.schemas.input_schemas import ComplexPasswordBody
from app.schemas.input_schemas import PasswordOptions
from app.schemas.input_schemas import PinPasswordOptions
from app.schemas.output_schemas import PasswordOutput
from app.use_cases.password import PasswordGenerator

_password_generator = Annotated[PasswordGenerator, Depends(PasswordGenerator)]
router = APIRouter(tags=["Password-Generator"])


@router.get("/", response_model=PasswordOutput)
async def get_password(service: _password_generator, password_options: PasswordOptions = Depends()):
    coroutines = [
        service.async_password(
            password_length=password_options.password_length,
            has_punctuation=password_options.has_punctuation,
        )
        for _ in range(password_options.quantity)
    ]
    results = await gather(*coroutines)
    return {"data": list(results)}


@router.get("/pin", response_model=PasswordOutput)
async def pin_code(service: _password_generator, password_options: PinPasswordOptions = Depends()):
    coroutines = [
        service.async_pin(pin_length=password_options.password_length) for _ in range(password_options.quantity)
    ]
    results = await gather(*coroutines)
    return {"data": list(results)}


@router.post("/complex_password", response_model=PasswordOutput)
async def complex_password(password_options: ComplexPasswordBody, pg: _password_generator):
    coroutines = [
        pg.async_complex_password(
            char_inject=password_options.char_inject,
            string_inject=password_options.string_inject,
            shuffle_string_inject=password_options.shuffle_string_inject,
            additional_length=password_options.additional_length,
            has_punctuation=password_options.punctuation,
        )
        for _ in range(password_options.quantity)
    ]
    results = await gather(*coroutines)
    return {"data": list(results)}
