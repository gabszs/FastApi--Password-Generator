# Testing the password class
import pytest

from app.use_cases.password import PasswordGenerator


@pytest.mark.asyncio
async def test_pin():
    password = PasswordGenerator()
    pin = await password.async_pin(pin_lenght=4)

    assert len(pin) == 4
    assert str(pin).isnumeric()
