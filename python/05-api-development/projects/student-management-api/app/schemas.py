from pydantic import BaseModel, ConfigDict, Field, model_validator


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=3, max_length=255)
    age: int = Field(ge=1, le=120)


class StudentUpdate(BaseModel):
    """Fields required to replace a student's complete record with PUT."""

    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=3, max_length=255)
    age: int = Field(ge=1, le=120)


class StudentPatch(BaseModel):
    """Optional fields for partial student updates with PATCH."""

    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: str | None = Field(default=None, min_length=3, max_length=255)
    age: int | None = Field(default=None, ge=1, le=120)

    @model_validator(mode="after")
    def validate_patch_fields(self):
        if not self.model_fields_set:
            raise ValueError("At least one field must be provided")
        if any(getattr(self, field) is None for field in self.model_fields_set):
            raise ValueError(
                "Fields cannot be null; omit fields you do not want to update"
            )
        return self


class StudentResponse(StudentCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int


class UserCreate(BaseModel):
    email: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class Token(BaseModel):
    access_token: str
    token_type: str
