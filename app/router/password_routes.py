from fastapi import (APIRouter, Path, Query)
from app.use_cases.password import PasswordGenerator
from app.schemas.Output_Scheme import PasswordOutput
from asyncio import gather


router = APIRouter(prefix='/password', tags=['Password-Generator'])


@router.get('/pin/{password_lenght}')
async def pin_code(password_lenght: int = Path(gt=0, le=100), quantity: int = Query(gt=0, le=100)):
    password = PasswordGenerator()
    corroutines = list()


    for number in range(quantity):
        coro = password.async_pin(pin_lenght=password_lenght)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    

    return PasswordOutput(
        message="Success",
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)]
    )