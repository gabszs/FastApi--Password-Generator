import re
from pydantic import (BaseModel, validator)
from typing import List
from app.schemas.custom_base_model import CustomBaseModel

class PasswordBody(CustomBaseModel):
    suffle_string_inject: bool = False
    char_inject: List[str]
    string_inject: List[str]

    @validator('char_inject')
    def validate_char_inject(cls, char_list):
        if any(len(char) != 1 for char in char_list):
            raise ValueError(f"Invalid Char Regex, The items in the list need to be only one ascii carachter")
        return char_list
    
    @validator('string_inject')
    def validate_string_inject(cls, string_list):
        if not any(re.match('.{2,}', string) for string in string_list):
            raise ValueError(f"Invalide String Regex, the items in the list need be more than one ascii charater")
        return string_list


if __name__ == "__main__":
    pb = PasswordBody(
        suffle_string_inject=False,
        char_inject=['s','b','_','2'],
        string_inject=["gabriel23%#@", "dudus1@"]
    )

    print(pb.dict())