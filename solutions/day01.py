
from collections import defaultdict
from typing import Dict, List, Tuple
from utils import read_file

def part1(left: List[int], right: List[int]) -> int:
    left.sort()
    right.sort()
    total = 0
    for l, r in zip(left, right):
        total += abs(l - r)
    return total

def part2(left: List[int], right: List[int]) -> int:
    freqs: Dict[int, int] = defaultdict(lambda: 0)
    for x in right:
        freqs[x] += 1
    return sum(x * freqs[x] for x in left)

if __name__ == '__main__':
    lines = read_file('day01.txt')
    s = [int(x) for y in lines for x in y.strip().split()]
    left = [s[x] for x in range(0, len(s)) if x % 2 == 0]
    right = [s[x] for x in range(0, len(s)) if x % 2 != 0]
    print(part1(left, right))
    print(part2(left, right))
