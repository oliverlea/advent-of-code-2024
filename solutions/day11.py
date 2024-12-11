from collections import defaultdict, deque
import math
from typing import Dict, List, Optional, Tuple, Set
from utils import read_file, within_bounds, Loc

def apply_rules(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    elif (int(math.log10(stone)) + 1) % 2 == 0:
        s = str(stone)
        middle = len(s) // 2
        return [int(s[:middle]), int(s[middle:])]
    else:
        return [stone * 2024]

def explore(stone: int, iterations: int) -> Dict[int, int]:
    freq: Dict[int, int] = defaultdict(lambda: 0)
    freq[stone] = 1
    for i in range(iterations):
        new_items: Dict[int, int] = defaultdict(lambda: 0)
        for s, f in freq.items():
            freq[s] = 0
            applied = apply_rules(s)
            for applied_stone in applied:
                new_items[applied_stone] += f
        freq = new_items
    return freq

def solve(stones: List[int], iterations: int) -> int:
    freqs: Dict[int, int] = defaultdict(lambda: 0)
    for stone in stones:
        explored = explore(stone, iterations)
        for s, f in explored.items():
            freqs[s] += f
    return sum(freqs.values())

if __name__ == '__main__':
    stones = [int(x) for x in read_file('day11.txt')[0].strip().split(" ")]
    print(solve(stones, iterations=25))
    print(solve(stones, iterations=75))