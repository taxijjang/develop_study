# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#callable-types-and-lambdas
# Callable types
from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 3))


def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


foo(add)
