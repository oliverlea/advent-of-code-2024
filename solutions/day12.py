from collections import defaultdict, deque
from typing import Dict, List, Tuple, Set
from utils import CARDINAL_DIRS, read_file, Loc, within_bounds

def fence(loc: Loc, grid: List[str]) -> Tuple[int, Set[Loc]]:
    target = grid[loc[1]][loc[0]]
    seen: Set[Loc] = set()
    q = deque()
    q.append(loc)
    fences = 0
    while q:
        cur = q.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        for d in CARDINAL_DIRS:
            nx, ny = (cur[0] + d[0], cur[1] + d[1])
            if within_bounds((nx, ny), grid) and grid[ny][nx] == target:
                q.append((nx, ny))
            else:
                fences += 1
    return fences, seen

def is_exposed(loc: Loc, direction: Tuple[int, int], area: Set[Loc]) -> bool:
    nx, ny = loc[0] + direction[0], loc[1] + direction[1]
    return (nx, ny) not in area

def perpendicular(direction: Tuple[int, int]) -> List[Tuple[int, int]]:
    if direction[0] != 0:
        return [(0, -1), (0, 1)]
    return [(-1, 0), (1, 0)]

def find_edge(start: Loc, exposure: Tuple[int, int], area: Set[Loc]) -> Set[Loc]:
    def edge_in_dir(cur_dir: Tuple[int, int]) -> Set[Loc]:
        result = set()
        q = deque()
        q.append(start)
        while q:
            cur = q.popleft()
            if cur in area and is_exposed(cur, exposure, area):
                result.add(cur)
                q.append((cur[0] + cur_dir[0], cur[1] + cur_dir[1]))
        return result

    total_result = set()
    total_result.add(start)
    for xdir in perpendicular(exposure):
        for new_edge_loc in edge_in_dir(xdir):
            total_result.add(new_edge_loc)
    return total_result

def discont_boundary_cost(full_cost: int, area: Set[Loc]) -> int:
    result = full_cost
    discounted: Dict[Loc, Set[Tuple[int, int]]] = defaultdict(set)
    for cur in area:
        for exposure_dir in CARDINAL_DIRS:
            if exposure_dir in discounted[cur]:
                continue
            edge = find_edge(cur, exposure_dir, area)
            if len(edge) > 1:
                result -= len(edge) - 1
                for e in edge:
                    discounted[e].add(exposure_dir)
    return result

def solve(grid: List[str], discount_fn = None) -> int:
    explored: Set[Loc] = set()
    result: Dict[str, int] = defaultdict(lambda: 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            loc = (x, y)
            if loc in explored:
                continue
            fences, expanded = fence(loc, grid)
            if discount_fn:
                fences = discount_fn(fences, expanded)
            result[grid[y][x]] += len(expanded) * fences
            for exp in expanded:
                explored.add(exp)
    return sum(result.values())

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day12.txt')]
    print(solve(lines))
    print(solve(lines, discount_fn=discont_boundary_cost))