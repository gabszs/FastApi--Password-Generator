# Testing the password class
import pytest
from app.use_cases.password import PasswordGenerator

@pytest.mark.asyncio
async def test_complex_pass_phrase():
    pg = PasswordGenerator()
    strings_list = ['Gab', 'tao', '2018']

    complex_password = await pg.async_complex_password(adicional_lenght=10,
                                                           has_ponctuation=True,
                                                           insert_string_List=strings_list
                                                           )


    assert len(complex_password) == 10 + sum(len(string) for string in strings_list)
    assert str(complex_password).isascii()
    assert any(char.isdigit() for char in complex_password)
    assert any(char.isalpha() for char in complex_password)
    assert any(char.isupper() for char in complex_password)
    assert any(char.islower() for char in complex_password)  
    assert all(complex_password.find(string) != -1 for string in strings_list)  



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

