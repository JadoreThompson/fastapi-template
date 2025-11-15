from pydantic import BaseModel
from typing import Generic, TypeVar


T = TypeVar("T")


class PaginationMeta(BaseModel):
    page: int
    size: int
    has_next: bool


class PaginatedResponse(PaginationMeta, Generic[T]):
    data: list[T]