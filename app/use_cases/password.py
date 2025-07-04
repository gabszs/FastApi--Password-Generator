# script to generate a Random Password
from random import shuffle
from secrets import choice
from string import ascii_letters
from string import digits
from string import punctuation
from typing import List

from app.core.telemetry import logger


class PasswordGenerator:
    """
    Class for generating random passwords and PIN codes.
    """

    async def async_pin(self, pin_lenght: int) -> int:
        pin_range = "1234567890"
        pin_choice = "".join(choice(pin_range) for _ in range(int(pin_lenght)))
        logger.info(f"Generated PIN of length {pin_lenght}")
        return pin_choice

    async def async_password(self, password_length: int, has_ponctuation: bool = False) -> str:
        minimum_string = choice(ascii_letters) + choice(digits) + choice(digits + ascii_letters)
        letters = ascii_letters + digits

        if has_ponctuation:
            minimum_string = list(minimum_string)
            del minimum_string[0]
            minimum_string = "".join(minimum_string)
            minimum_string += choice(punctuation)
            letters += punctuation
            logger.info("Punctuation enabled for password generation")

        if password_length == 3:
            password = "".join(choice(minimum_string) for _ in range(len(minimum_string)))
            logger.info("Generated short password with length 3")
            return PasswordGenerator.lower_upper_func(password)
        else:
            password_choice = "".join(choice(letters) for _ in range(password_length - 3)) + minimum_string
            password_list = list(password_choice)
            shuffle(password_list)
            password = "".join(password_list)
            logger.info(f"Generated password of length {password_length}")
            return PasswordGenerator.lower_upper_func(password)

    async def async_complex_password(
        self,
        char_inject: List[str],
        string_inject: List[str],
        suffle_string_inject: bool = False,
        adicional_lenght: int = 0,
        has_ponctuation: bool = False,
    ) -> str:
        password = await self.async_password(password_length=adicional_lenght, has_ponctuation=has_ponctuation)

        if suffle_string_inject:
            logger.info("Shuffling injected strings")
            for count, string in enumerate(string_inject):
                string = list(string)
                shuffle(string)
                string_inject[count] = "".join(string)

        password = list(password)
        [password.append(item) for item in string_inject]
        [password.append(item) for item in char_inject]
        shuffle(password)

        password = "".join(password)
        logger.info(
            f"Generated complex password with {len(string_inject)} injected strings and {len(char_inject)} characters"
        )
        return password

    @classmethod
    def lower_upper_func(cls, password: str) -> str:
        if password.upper() == password:
            password = list(password)
            randchoice = choice(list(range(len(password))))
            num = password[randchoice]
            while not num.isalpha():
                randchoice = choice(list(range(len(password))))
                num = password[randchoice]
            password[randchoice] = password[randchoice].lower()
            logger.info("Adjusted all-uppercase password by lowering one character")
            return "".join(password)

        elif password.lower() == password:
            password = list(password)
            randchoice = choice(list(range(len(password))))
            num = password[randchoice]
            while not num.isalpha():
                randchoice = choice(list(range(len(password))))
                num = password[randchoice]
            password[randchoice] = password[randchoice].upper()
            logger.info("Adjusted all-lowercase password by uppercasing one character")
            return "".join(password)

        return password
