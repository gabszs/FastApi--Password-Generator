from pydantic import (validator)
from app.schemas.custom_base_model import CustomBaseModel
from typing import List
from pydantic import (validator)


class PasswordOutput(CustomBaseModel):
    message: str
    data: List[dict]


    