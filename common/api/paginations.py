from typing import Any, Generic, TypeVar

from django.conf import settings
from django.db.models import QuerySet
from ninja import Field, Schema
from ninja.pagination import PaginationBase

T = TypeVar("T")


class GenericLimitOffsetPagination(PaginationBase, Generic[T]):
    """Для QuerySet с декоратором @paginate."""

    class Input(Schema):
        limit: int = Field(default=settings.PAGINATION_PER_PAGE, ge=1, le=100)
        offset: int = Field(0, ge=0)

    class Output(Schema, Generic[T]):  # type: ignore[name-defined]
        next_page: bool
        results: list[T]
        count: int

    items_attribute: str = "results"

    @staticmethod
    def paginate_queryset(
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> dict[str, Any]:
        count = queryset.count()
        start = pagination.offset
        end = start + pagination.limit
        return {
            "next_page": end < count,
            "results": list(queryset[start:end]),
            "count": count,
        }