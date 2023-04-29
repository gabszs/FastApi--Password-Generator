from pydantic import (BaseModel)
from typing import List

class PasswordOutput(BaseModel):
    message: str
    data: List[dict]
    
    