# Testing the password class
import pytest

from app.use_cases.password import PasswordGenerator


@pytest.mark.asyncio
async def test_ponctuation_password():
    pg = PasswordGenerator()
    password_ponctuation = await pg.async_password(password_lenght=10, has_ponctuation=True)

    assert len(password_ponctuation) == 10
    assert str(password_ponctuation).isascii()
    assert any(char.isdigit() for char in password_ponctuation)
    assert any(char.isalpha() for char in password_ponctuation)


@pytest.mark.asyncio
async def test_no_ponctutation_password():
    pg = PasswordGenerator()
    password = await pg.async_password(password_lenght=5)

    assert len(password) == 5
    assert str(password).isalnum()
    assert any(char.isdigit() for char in password)
    assert any(char.isalpha() for char in password)
