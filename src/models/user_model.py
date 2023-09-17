from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    id: int
    name: str
    role: str | None
    age: str
    phone: str | None
    email: EmailStr | None
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    role: str | None
    age: str
    phone: str | None
    email: EmailStr | None
