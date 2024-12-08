
from collections import defaultdict
from typing import Dict, List, Optional, Set
from utils import distance, read_file, within_bounds, Loc

def map_nodes(lines: List[str]) -> Dict[str, List[Loc]]:
    nodes: Dict[str, List[Loc]] = defaultdict(list)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cur = lines[y][x]
            if cur != '.':
                nodes[cur].append((x, y))
    return nodes

def apply_diff(loc: Loc, diff: Loc) -> Loc:
    return loc[0] + diff[0], loc[1] + diff[1]

def solve(lines: List[str], iterations: Optional[int] = 1) -> Set[Loc]:
    nodes = map_nodes(lines)
    result: Set[Loc] = set()
    for locs in nodes.values():
        for i in range(len(locs)):
            cur = locs[i]
            for p in range(i + 1, len(locs)):
                pair = locs[p]
                d = distance(cur, pair)
                for start, diff in [(cur, d), (pair, (-d[0], -d[1]))]:
                    origin = apply_diff(start, diff)
                    found = 0
                    while (iterations is None or found < iterations) and within_bounds(origin, lines):
                        result.add(origin)
                        found += 1
                        origin = apply_diff(origin, diff)
    return result

def part1(lines: List[str]) -> int:
    antinodes = solve(lines, iterations=1)
    return len(antinodes)

def part2(lines: List[str]) -> int:
    antinodes = solve(lines, iterations=None)
    result = len(antinodes)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != '.' and (x, y) not in antinodes:
                result += 1
    return result

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day08.txt')]
    print(part1(lines))
    print(part2(lines))