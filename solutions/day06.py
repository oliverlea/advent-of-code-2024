
from typing import Dict, List, Optional, Tuple, Set
from utils import read_file, within_bounds

DIR_MASK: Dict[str, Tuple[int, int]] = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}
DIR_NEXT: Dict[str, str] = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

def find_guard(lines: List[str]) -> Tuple[int, int]:
    dirs = DIR_MASK.keys()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] in dirs:
                return (x, y)
    raise ValueError()

def move(start: Tuple[int, int], dir: Tuple[int, int], lines: List[str], additional_obstacle: Optional[Tuple[int, int]] = None) -> List[Tuple[int, int]]:
    cur = start
    result: List[Tuple[int, int]] = []
    while within_bounds(cur, lines) and lines[cur[1]][cur[0]] != '#':
        if additional_obstacle and cur == additional_obstacle:
            break
        result.append(cur)
        cur = (cur[0] + dir[0], cur[1] + dir[1])
    if not within_bounds(cur, lines):
        result.append(cur)
    return result

def find_path(guard_start: Tuple[int, int], dir: str, lines: List[str]) -> List[Tuple[int, int]]:
    cur = guard_start
    path: List[Tuple[int, int]] = []
    while within_bounds(cur, lines):
        moved = move(cur, DIR_MASK[dir], lines)
        if moved:
            for loc in moved:
                if within_bounds(loc, lines):
                    path.append(loc)
            cur = moved[-1]
        dir = DIR_NEXT[dir]
    return path

def part1(lines: List[str]) -> int:
    guard = find_guard(lines)
    dir = lines[guard[1]][guard[0]]
    return len(set(find_path(guard, dir, lines)))

def loops(guard_start: Tuple[int, int], dir: str, new_obstacle: Tuple[int, int], lines: List[str]) -> bool:
    cur = guard_start
    been: Set[Tuple[Tuple[int, int], str]] = set()
    while within_bounds(cur, lines):
        moved = move(cur, DIR_MASK[dir], lines, additional_obstacle=new_obstacle)
        if moved:
            dest = moved[-1]
            if not within_bounds(dest, lines):
                return False
            if ((dest, dir)) in been:
                return True
            been.add((dest, dir))
            cur = dest
        dir = DIR_NEXT[dir]
    return False

def part2(lines: List[str]) -> int:
    guard = find_guard(lines)
    dir = lines[guard[1]][guard[0]]
    path = find_path(guard, dir, lines)[1:]
    spath = set()
    path = [x for x in path if not (x in spath or spath.add(x) or x == guard)]
    loop_count = [new_obs for new_obs in path if loops(guard, dir, new_obs, lines)]
    return len(loop_count)

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day06.txt')]
    print(part1(lines))
    print(part2(lines))