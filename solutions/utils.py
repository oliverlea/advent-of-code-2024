
from typing import Any, List, Tuple, TypeVar, Union

EXPAND = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

CARDINAL_DIRS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def read_file(fn: str) -> List[str]:
    with open('./input/' + fn, 'r') as f:
        return f.readlines()

Loc = Tuple[int, int]

def search(lines: List[str], coord: Loc, target: str) -> bool:
    if not target:
        return True
    x, y = coord
    if y >= len(lines) or y < 0 or x >= len(lines[0]) or x < 0:
        return False
    if lines[y][x] != target[0]:
        return False
    next_target = target[1:]
    for (xn, yn) in EXPAND:
        if search(lines, (x + xn, y + yn), next_target):
            return True
    return False

T = TypeVar("T")
Grid = Union[List[List[T]], List[str]]

def grid_at(target: Grid, loc: Loc):
    return target[loc[1]][loc[0]]

def within_bounds(loc: Loc, target: Grid) -> bool:
    x, y = loc
    if y >= len(target) or y < 0 or x >= len(target[0]) or x < 0:
        return False
    return True

def expand(loc: Loc) -> List[Loc]:
    result = [(0, 0)] * 4
    for i, direction in enumerate(CARDINAL_DIRS):
        result[i] = (loc[0] + direction[0], loc[1] + direction[1])
    return result

def distance(l1: Loc, l2: Loc) -> Loc:
    x = l1[0] - l2[0]
    y = l1[1] - l2[1]
    return x, y
