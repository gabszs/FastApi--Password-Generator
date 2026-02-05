# Testing the password class
import pytest

from app.use_cases.password import PasswordGenerator


@pytest.mark.asyncio
async def test_punctuation_password():
    pg = PasswordGenerator()
    password = await pg.async_password(password_length=10, has_punctuation=True)

    assert len(password) == 10
    assert str(password).isascii()
    assert any(char.isdigit() for char in password)
    assert any(char.isalpha() for char in password)


@pytest.mark.asyncio
async def test_no_punctuation_password():
    pg = PasswordGenerator()
    password = await pg.async_password(password_length=5)

    assert len(password) == 5
    assert str(password).isalnum()
    assert any(char.isdigit() for char in password)
    assert any(char.isalpha() for char in password)
