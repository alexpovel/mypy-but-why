import typing as t

import pytest


def add_numbers(a: int, b: int) -> int:
    return a + b


IRRELEVANT = object()


@pytest.mark.parametrize(
    ["a", "b", "result"],
    [(1, 2, 3)],
)
def test_add_numbers(a: t.Any, b: t.Any, result: t.Any) -> None:
    assert add_numbers(a, b) == result


# ❓❓❓ What quack?
#
# Duck typing is solved differently now.
