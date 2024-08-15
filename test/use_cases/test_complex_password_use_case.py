# Testing the password class
import pytest

from app.use_cases.password import PasswordGenerator


@pytest.mark.asyncio
async def test_complex_password_no_suffle():
    pg = PasswordGenerator()
    strings_list = ["Gab", "tao", "2018"]
    char_list = ["a", "b", "/0"]

    complex_password = await pg.async_complex_password(
        char_inject=char_list,
        adicional_lenght=10,
        has_ponctuation=True,
        string_inject=strings_list,
        suffle_string_inject=False,
    )

    assert len(complex_password) == 10 + sum(
        [
            sum(len(string) for string in strings_list),
            sum(len(char) for char in char_list),
        ]
    )
    assert str(complex_password).isascii()
    assert any(char.isdigit() for char in complex_password)
    assert any(char.isalpha() for char in complex_password)
    assert any(char.isupper() for char in complex_password)
    assert any(char.islower() for char in complex_password)
    assert all(complex_password.find(string) != -1 for string in strings_list)

    # async def test():
    # password = await pg.async_complex_password(
    #     char_inject=['a', 'b', '/0'],
    #     adicional_lenght=10,
    #     has_ponctuation=True,
    #     string_inject=['Gab', 'tao', '2018'],
    #     suffle_string_inject=False
    # )
    #     return password


# @pytest.mark.asyncio
# async def test_no_ponctutation_password():
#     pg = PasswordGenerator()
#     password = await pg.async_password(password_lenght=5)


#     assert len(password) == 5
#     assert str(password).isalnum()
#     assert any(char.isdigit() for char in password)
#     assert any(char.isalpha() for char in password)
#     assert any(char.isupper() for char in password)
#     assert any(char.islower() for char in password)
