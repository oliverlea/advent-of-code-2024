    
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set
from utils import distance, read_file, within_bounds, Loc

DIR_MASK = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def score(loc: Loc, inputs: List[str], *, all_routes: bool) -> int:
    trail_ends: Set[Loc] = set()
    def rscore(cur: Loc) -> int:
        x, y = cur
        cur_value = inputs[y][x]
        if cur_value == '9':
            if all_routes:
                return 1
            elif cur not in trail_ends:
                trail_ends.add(cur)
                return 1
            return 0
        else:
            target = str(int(inputs[y][x]) + 1)
            r_results = []
            for x_dir, y_dir in DIR_MASK:
                next_loc = (x + x_dir, y + y_dir)
                nx, ny = next_loc
                if within_bounds(next_loc, inputs) and inputs[ny][nx] == target:
                    r_results.append(rscore(next_loc))
            return sum(r_results)

    return rscore(loc)

def calculate(inputs: List[str], all_routes: bool = False) -> int:
    result = 0
    for y in range(len(inputs)):
        for x in range(len(inputs[0])):
            if inputs[y][x] == '0':
                result += score((x, y), inputs, all_routes=all_routes)
    return result

if __name__ == '__main__':
    inputs = [x.strip() for x in read_file('day10.txt')]
    print(calculate(inputs, all_routes=False))
    print(calculate(inputs, all_routes=True))