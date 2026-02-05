from pydantic import BaseModel
from pydantic import Field


class PasswordOutput(BaseModel):
    data: list[str] = Field(..., examples=[["aB3$kLm9", "xR7!pQn2"]])
