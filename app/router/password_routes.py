from fastapi import (APIRouter, Path, Query)
from app.use_cases.password import PasswordGenerator
from app.schemas.Output_Scheme import PasswordOutput
from asyncio import gather


router = APIRouter(prefix='/password', tags=['Password-Generator'])


@router.get('/pin/{password_lenght}', response_model=PasswordOutput, response_model=PasswordOutput)
async def pin_code(password_lenght: int = Path(gt=0, le=100), quantity: int = Query(gt=0, le=100)):
    """
    Endpoint to generate random pin codes.
    
    Parameters:
    -----------
    password_lenght : int
        The length of the pin code to be generated.
    
    quantity : int
        The number of pin codes to be generated.
    
    Returns:
    --------
    PasswordOutput
        An object containing a message and a list of dictionaries, each containing a number and its respective pin code.
    """    

    pg = PasswordGenerator()
    corroutines = list()


    for number in range(quantity):
        coro = pg.async_pin(pin_lenght=password_lenght)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    

    return PasswordOutput(
        message="Success",
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)]
    )


@router.get('/pass/{password_lenght}', response_model=PasswordOutput)
async def pass_code(password_lenght: int = Path(gt=0, le=100), quantity: int = Query(gt=0, le=100), ponctuation: bool = False):
    """
    Endpoint to generate random passwords.
    
    Parameters:
    -----------
    password_lenght : int
        The length of the password to be generated.
    
    quantity : int
        The number of passwords to be generated.
    
    ponctuation : bool, optional
        A boolean value indicating whether the password should contain punctuation characters.
    
    Returns:
    --------
    PasswordOutput
        An object containing a message and a list of dictionaries, each containing a number and its respective password.
    """     
    pg = PasswordGenerator()
    """
    Endpoint to generate random pin codes.
    
    Parameters:
    -----------
    password_lenght : int
        The length of the pin code to be generated.
    
    quantity : int
        The number of pin codes to be generated.
    
    Returns:
    --------
    PasswordOutput
        An object containing a message and a list of dictionaries, each containing a number and its respective pin code.
    """    

    pg = PasswordGenerator()
    corroutines = list()


    for number in range(quantity):
        coro = pg.async_password(password_lenght=password_lenght, has_ponctuation=ponctuation)
        coro = pg.async_pin(pin_lenght=password_lenght)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    

    return PasswordOutput(
        message="Success",
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)]
    )


@router.get('/pass/{password_lenght}', response_model=PasswordOutput)
async def pass_code(password_lenght: int = Path(gt=0, le=100), quantity: int = Query(gt=0, le=100), ponctuation: bool = False):
    """
    Endpoint to generate random passwords.
    
    Parameters:
    -----------
    password_lenght : int
        The length of the password to be generated.
    
    quantity : int
        The number of passwords to be generated.
    
    ponctuation : bool, optional
        A boolean value indicating whether the password should contain punctuation characters.
    
    Returns:
    --------
    PasswordOutput
        An object containing a message and a list of dictionaries, each containing a number and its respective password.
    """     
    pg = PasswordGenerator()
    corroutines = list()



    for number in range(quantity):
        coro = pg.async_password(password_lenght=password_lenght, has_ponctuation=ponctuation)
        corroutines.append(coro)

    gather_result = await gather(*corroutines)
    

    return PasswordOutput(
        message="Success",
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)]
    )

