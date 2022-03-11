from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# type alias

Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]] = 17

X = int
x: X = 8

value: Value = 17


def cal(v: Value) -> Value:
    return v


# dict alias

ddd = Dict[str, str] = {'hello': 'world', 'world': 'wow!!', 'hee': '17'}


class Point(TypedDict):
    x: int
    y: float
    z: str
