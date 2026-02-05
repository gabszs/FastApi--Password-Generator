from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator


class PinPasswordOptions(BaseModel):
    password_length: int = Field(default=12, gt=2, le=200, description="Length of the generated PIN")
    quantity: int = Field(default=1, gt=0, le=100, description="Number of PINs to generate")


class PasswordOptions(PinPasswordOptions):
    has_punctuation: bool = Field(default=True, description="Include punctuation characters")


class ComplexPasswordBody(BaseModel):
    additional_length: int = Field(..., gt=0, le=100, description="Extra random characters to add")
    quantity: int = Field(default=1, gt=0, le=100, description="Number of passwords to generate")
    punctuation: bool = Field(default=False, description="Include punctuation characters")
    shuffle_string_inject: bool = Field(default=False, description="Shuffle injected strings before inserting")
    char_inject: list[str] = Field(
        default_factory=list,
        description="List of single characters to inject",
        examples=[["a", "1", "@"]],
    )
    string_inject: list[str] = Field(
        default_factory=list,
        description="List of strings (2+ chars) to inject",
        examples=[["hello", "world"]],
    )

    @field_validator("char_inject")
    @classmethod
    def validate_char_inject(cls, char_list: list[str]) -> list[str]:
        for char in char_list:
            if len(char) != 1:
                raise ValueError(f"Each item must be exactly 1 character, got '{char}' with length {len(char)}")
        return char_list

    @field_validator("string_inject")
    @classmethod
    def validate_string_inject(cls, string_list: list[str]) -> list[str]:
        for string in string_list:
            if len(string) < 2:
                raise ValueError(f"Each item must have at least 2 characters, got '{string}'")
        return string_list
