# Testing the password class
import pytest

from app.use_cases.password import PasswordGenerator


@pytest.mark.asyncio
async def test_complex_password_no_shuffle():
    pg = PasswordGenerator()
    strings_list = ["Gab", "tao", "2018"]
    char_list = ["a", "b", "/0"]

    complex_password = await pg.async_complex_password(
        char_inject=char_list,
        additional_length=10,
        has_punctuation=True,
        string_inject=strings_list,
        shuffle_string_inject=False,
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
