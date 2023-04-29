# script to generate a Random Password
from schemas.Input_scheme import PasswordBody
from secrets import choice
from random import shuffle
from string import (ascii_letters, digits, punctuation)
from asyncio import (gather, get_event_loop)



class PasswordGenerator:
    """
    Class for generating random passwords and PIN codes.

    Methods:
    async_pin(pin_lenght: int) -> int:
        Generates a random PIN code with the given length.
    
    async_password(password_lenght: int, has_ponctuation: bool = False) -> str:
        Generates a random password with the given length and optionally with punctuations.
    """

    async def async_pin(self, pin_lenght: int) -> int:
        """
        Generates a random PIN code with the given length.

        Args:
        pin_lenght (int): The length of the generated PIN code.

        Returns:
        int: The generated PIN code.
        """        
        pin_range = '1234567890'
        pin_choice = ''.join(choice(pin_range) for _ in range(int(pin_lenght)))
        return pin_choice
    

    async def async_password(self, password_lenght: int, has_ponctuation: bool = False) -> str: 
        """
        Generates a random password with the given length and optionally with punctuations.

        Args:
        password_lenght (int): The length of the generated password.
        has_ponctuation (bool, optional): Whether or not to include punctuations in the password. Defaults to False.

        Returns:
        str: The generated password.
        """
        minimum_string = choice(ascii_letters) + choice(digits) + choice(digits + ascii_letters)
        letters = ascii_letters + digits
        
        if has_ponctuation:
            minimum_string = list(minimum_string)
            del minimum_string[0]
            minimum_string = "".join(minimum_string)

            minimum_string += choice(punctuation)
            letters += punctuation

        
        if password_lenght == 3:
            password = ''.join(choice(minimum_string) for _ in len(minimum_string))
            return PasswordGenerator.lower_upper_func(password)
        
        else:
            password_choice = ''.join(choice(letters) for _ in range(password_lenght - 3)) + minimum_string
            password_list = list(password_choice)
            shuffle(password_list)
            password = "".join(password_list)
            return PasswordGenerator.lower_upper_func(password)
        

    async def async_complex_password(self, body: PasswordBody,
                                     adicional_lenght: int = 0,
                                     has_ponctuation: bool = False) -> str:
        shuffle_string, chars , string_list = body.suffle_string_inject, body.char_inject, body.string_inject
        password = await self.async_password(password_lenght=adicional_lenght, has_ponctuation=has_ponctuation)

        if shuffle_string:
            string_list = ["".join(shuffle(list(item))) for item in string_list]

        password = list(password)
        [password.append(item) for item in string_list]
        [password.append(item) for item in chars]
        shuffle(password)

        password = ''.join(password)

        return password



    # async_complex_password(adicional_lenght=10,
    #                                                        has_ponctuation=True,
    #                                                        insert_string_List=strings_list
    #                                                        )

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
                return ''.join(password)     

            elif password.lower() == password:
                password = list(password)
                randchoice = choice(list(range(len(password))))
                num = password[randchoice]

                while not num.isalpha():
                    randchoice = choice(list(range(len(password))))  
                    num = password[randchoice]

                password[randchoice] = password[randchoice].upper()
                return ''.join(password) 

            else:
                return password

if __name__ == "__main__":
    pg = PasswordGenerator()

    result = gather(PasswordGenerator().async_pin(pin_lenght=5))

    async def test():
        lst = []
        for _ in range(3):
            lst.append(pg.async_password(password_lenght=5, has_ponctuation=True))
        
        gather_result = await gather(*lst)
        print([{f"pass {count}": gather_result[count]} for count in range(19)])

    async def main():
        await pg.async_password(password_lenght=5, has_ponctuation=True)

    loop = get_event_loop()
    loop.run_until_complete(main())
