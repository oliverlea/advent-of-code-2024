
from typing import Any, List, Tuple

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

def read_file(fn: str) -> List[str]:
    with open('./input/' + fn, 'r') as f:
        return f.readlines()

def search(lines: List[str], coord: Tuple[int, int], target: str) -> bool:
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

def within_bounds(loc: Tuple[int, int], target: List[Any]) -> bool:
    x, y = loc
    if y >= len(target) or y < 0 or x >= len(target[0]) or x < 0:
        return False
    return True
