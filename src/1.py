from contextlib import nullcontext as does_not_raise

import pytest


def add_numbers(a, b):
    return a + b


IRRELEVANT = object()


@pytest.mark.parametrize(
    ["a", "b", "result", "expectation"],
    [
        (1, 2, 3, does_not_raise()),
        ("a", "b", "ab", does_not_raise()),
        (1, None, IRRELEVANT, pytest.raises(TypeError)),
        (None, 1, IRRELEVANT, pytest.raises(TypeError)),
        (None, None, IRRELEVANT, pytest.raises(TypeError)),
    ],
)
def test_add_numbers(a, b, result, expectation):
    with expectation:
        assert add_numbers(a, b) == result
