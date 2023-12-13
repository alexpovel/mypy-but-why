import typing as t

import pytest

T = t.TypeVar("T")


class Addable(t.Protocol):
    def __add__(self: T, other: T) -> T:
        ...


K = t.TypeVar("K", bound=Addable)


def add_numbers(a: K, b: K) -> K:
    return a + b


IRRELEVANT = object()


@pytest.mark.parametrize(
    ["a", "b", "result"],
    [
        (1, 2, 3),
        ("a", "b", "ab"),
    ],
)
def test_add_numbers(a: t.Any, b: t.Any, result: t.Any) -> None:
    assert add_numbers(a, b) == result


# ❗❗❗ That's ugly.
#
# Python 3.12 has an answer for that:


# def add_numbers_again[A: Addable](a: A, b: A) -> A:
#     return a + b
