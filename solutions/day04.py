
from typing import List, Optional, Tuple
from utils import read_file, within_bounds

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

SAM_MASKS = [
    [
        (-1, -1),
        (0, 0),
        (1, 1)
    ],
    [
        (1, -1),
        (0, 0),
        (-1, 1)
    ]
]

def search_direction(lines: List[str], coord: Tuple[int, int], direction:  Tuple[int, int], target: str) -> bool:
    x, y = coord
    while target:
        if y >= len(lines) or y < 0 or x >= len(lines[0]) or x < 0:
            return False
        if lines[y][x] != target[0]:
            return False
        target = target[1:]
        x += direction[0]
        y += direction[1]
    return True

def part1(lines: List[str]) -> int:
    result = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            cur = (x, y)
            for dir in EXPAND:
                if search_direction(lines, cur, dir, 'XMAS'):
                    result += 1
    return result

def part2(lines: List[str]) -> int:
    def extract_mask(cur: Tuple[int, int], mask: List[Tuple[int, int]]) -> Optional[str]:
        mask_result: List[str] = []
        for m in mask:
            x = cur[0] + m[0]
            y = cur[1] + m[1]
            if not within_bounds((x, y), lines):
                return None
            mask_result.append(lines[y][x])
        return "".join(mask_result)
    result = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            valid = True
            for mask in SAM_MASKS:
                if extract_mask((x, y), mask) not in {"SAM", "MAS"}:
                    valid = False
                    break
                else:
                    pass
            if valid:
                result += 1
    return result

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day04.txt')]
    print(part1(lines))
    print(part2(lines))