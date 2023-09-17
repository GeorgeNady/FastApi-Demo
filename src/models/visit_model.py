from pydantic import BaseModel


class Visit(BaseModel):
    id: int
    title: str
