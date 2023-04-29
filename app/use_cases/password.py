
# script to generate a Random Password
from secrets import choice
from string import (ascii_letters, digits, punctuation)
from asyncio import gather


class PasswordGenerator:
    async def async_pin(self, pin_lenght: int) -> int:
        """
        Function to generate a pin password, parameter pin_leng is int to decide the size of the pin
        :param pin_lenght: int
        :return: str
        """
        pin_range = '1234567890'
        pin_choice = ''.join(choice(pin_range) for _ in range(int(pin_lenght)))
        return pin_choice


if __name__ == "__main__":
    result = gather(PasswordGenerator().async_pin(pin_lenght=5))
    print(result)











    # def pin(pin_lenght):
    #     """
    #     Function to generate a pin password, parameter pin_leng is int to decide the size of the pin
    #     :param pin_lenght: int
    #     :return: str
    #     """
    #     pin_range = '1234567890'
    #     pin_choice = ''.join(choice(pin_range) for _ in range(int(pin_lenght)))
    #     return pin_choice


    # def password(password_lenght, ponctuation=False):
    #     """
    #     Function to generate a password with letters and digits, and punctuations if necessary
    #     :param password_lenght: str
    #     :param ponctuation: Bool
    #     :return:
    #     """
    #     if ponctuation is True:  # if punctuation equals to True, letters going to have punctuation
    #         letters = ascii_letters + digits + punctuation
    #     else:  # else letters going to have only letters and digits
    #         letters = ascii_letters + digits
    #     password_choice = ''.join(choice(letters) for _ in range(password_lenght))
    #     # concatenate the letters to create a password
    #     return password_choice


    # print(password(10, ponctuation=False))