
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

def find_path(guard_start: Tuple[int, int], dir: str, lines: List[str]) -> List[Tuple[Tuple[int, int], str]]:
    """
    Return type is (location, dir), where dir is the direction the guard is facing after finding an obstacle.
    For example, for any move in which the guard moves forward freely the direction will be the direction
    of momentum. If the guard reaches an obstacle, the direction will be 90o right from the original direction
    of momentum.
    """
    cur = guard_start
    path: List[Tuple[Tuple[int, int], str]] = []
    while within_bounds(cur, lines):
        moved = move(cur, DIR_MASK[dir], lines)
        if moved:
            for loc in moved:
                if within_bounds(loc, lines):
                    if loc == moved[-1]:
                        path.append((loc, DIR_NEXT[dir]))
                    else:
                        path.append((loc, dir))
            cur = moved[-1]
        dir = DIR_NEXT[dir]
    return path

def part1(lines: List[str]) -> int:
    guard = find_guard(lines)
    dir = lines[guard[1]][guard[0]]
    return len(set(x[0] for x in find_path(guard, dir, lines)))

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
    path = [x for x in path if not (x[0] in spath or spath.add(x[0]) or x[0] == guard)]
    # return sum(1 for new_obs in path if loops(guard, dir, new_obs[0], lines))
    
    # optimize slightly by only searching for loops from the original path and skipping
    # all of the movement up until the preceding guards location on the original path
    prev_guard = guard
    prev_guard_dir = dir
    result = 0
    for loc, new_dir in path:
        if loops(prev_guard, prev_guard_dir, loc, lines):
            result += 1
        prev_guard = loc
        prev_guard_dir = new_dir

    return result

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day06.txt')]
    print(part1(lines))
    print(part2(lines))