from asyncio import gather

from fastapi import APIRouter
from fastapi import Path
from fastapi import Query

from app.schemas.Input_scheme import PasswordBody
from app.schemas.Output_Scheme import PasswordOutput
from app.use_cases.password import PasswordGenerator


router = APIRouter(tags=["Password-Generator"])


@router.get("/", response_model=PasswordOutput)
async def get_code():
    """
    Endpoint to generate random PIN codes With 12 chars and ponctuation.

    Returns:
    --------
    PasswordOutput
        An object containing a message and a list of dictionaries, each containing the PIN code.
    """
    pg = PasswordGenerator()

    password = await pg.async_password(password_lenght=12, has_ponctuation=True)

    return PasswordOutput(message="Success", data=[{"1º pin": password}])


@router.get("/pin/{password_lenght}", response_model=PasswordOutput)
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
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)],
    )


@router.get("/pass/{password_lenght}", response_model=PasswordOutput)
async def pass_code(
    password_lenght: int = Path(gt=0, le=100),
    quantity: int = Query(gt=0, le=100),
    ponctuation: bool = False,
):
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
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)],
    )


@router.post("/complex_password/{adicional_lenght}", response_model=PasswordOutput)
async def complex_password(
    body: PasswordBody,
    adicional_lenght: int = Path(gt=0, le=100),
    quantity: int = Query(gt=0, le=100),
    ponctuation: bool = False,
):
    """
    POST /complex_password/{additional_length}

    Generate a list of complex passwords.

    Path Parameters:
    - additional_length (int): The additional length to be added to each generated password. Must be a positive integer between 1 and 100, inclusive.

    Query Parameters:
    - quantity (int): The number of passwords to be generated. Must be a positive integer between 1 and 100, inclusive. Default value is 1.
    - punctuation (bool): If set to true, the generated passwords will contain at least one punctuation character. Default value is false.

    Request Body:
    - suffle_string_inject (bool): If set to true, the order of the string injections will be randomized in each generated password. Default value is false.
    - char_inject (List[str]): A list of ASCII characters that will be injected into each generated password. Each item in the list must be a string of length 1.
    - string_inject (List[str]): A list of strings that will be injected into each generated password. Each item in the list must be a string of length 2 or greater.

    Response:
    - message (str): A message indicating whether the operation was successful.
    - data (List[Dict[str, str]]): A list of dictionaries, each containing the generated password as a value and its position in the list as a key. Each generated password will contain at least one numeric and one alphabetic character. If punctuation is set to true, each generated password will also contain at least one punctuation character.

    """
    pg = PasswordGenerator()
    corroutines = list()

    for number in range(quantity):
        coro = pg.async_complex_password(
            char_inject=body.char_inject,
            string_inject=body.string_inject,
            suffle_string_inject=body.suffle_string_inject,
            adicional_lenght=adicional_lenght,
            has_ponctuation=ponctuation,
        )
        corroutines.append(coro)

    gather_result = await gather(*corroutines)

    return PasswordOutput(
        message="Success",
        data=[{f"{count + 1}º pin": gather_result[count]} for count in range(quantity)],
    )
