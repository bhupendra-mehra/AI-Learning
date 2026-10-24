from dataclasses import dataclass
from math import ceil
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Pagination(Generic[T]):
    items: list[T]
    page: int
    per_page: int
    total: int

    @property
    def pages(self) -> int:
        """Return the total number of pages."""
        if self.total == 0:
            return 0

        return ceil(self.total / self.per_page)

    @property
    def has_prev(self) -> bool:
        """Return True if a previous page exists."""
        return self.page > 1

    @property
    def has_next(self) -> bool:
        """Return True if a next page exists."""
        return self.page < self.pages

    @property
    def prev_num(self) -> int | None:
        """Return the previous page number."""
        if not self.has_prev:
            return None

        return self.page - 1

    @property
    def next_num(self) -> int | None:
        """Return the next page number."""
        if not self.has_next:
            return None

        return self.page + 1

    @property
    def first(self) -> int:
        """Return the first item number displayed on the current page."""
        if self.total == 0:
            return 0

        return (self.page - 1) * self.per_page + 1

    @property
    def last(self) -> int:
        """Return the last item number displayed on the current page."""
        return min(self.page * self.per_page, self.total)

    def iter_pages(
        self,
        left_edge: int = 1,
        left_current: int = 2,
        right_current: int = 2,
        right_edge: int = 1,
    ):
        """
        Generate page numbers for pagination navigation.

        None represents a gap (...).
        """

        last = 0

        for num in range(1, self.pages + 1):

            if (
                num <= left_edge
                or num > self.pages - right_edge
                or (
                    num >= self.page - left_current and num <= self.page + right_current
                )
            ):

                if last + 1 != num:
                    yield None

                yield num

                last = num
