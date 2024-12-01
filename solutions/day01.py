
from collections import defaultdict
from typing import Dict, List, Tuple
from utils import read_file

def part1(left: List[int], right: List[int]) -> int:
    return sum(abs(l - r) for l, r in zip(left, right))

def part2(left_sorted: List[int], right_sorted: List[int]) -> int:
    # 'optimized' solution using two pointers that relies on the input
    # already being sorted to solve in linear time
    result = 0
    li, ri = 0, 0
    dist = 0
    while li < len(left_sorted):
        while right_sorted[ri] < left_sorted[li]:
            ri += 1
            if ri >= len(right_sorted):
                break
        if left_sorted[li] == right_sorted[ri]:
            dist = 0
            while ri < len(right_sorted) and left_sorted[li] == right_sorted[ri]:
                dist += 1
                ri += 1
            repeats = 0
            while li + 1 < len(left_sorted) and left_sorted[li + 1] == left_sorted[li]:
                repeats += 1
                li += 1
            result += (left_sorted[li] * dist) * (repeats + 1)
            li += 1
        else:
            li += 1

    return result

if __name__ == '__main__':
    lines = read_file('day01.txt')
    s = [int(x) for y in lines for x in y.strip().split()]
    left = [s[x] for x in range(0, len(s)) if x % 2 == 0]
    right = [s[x] for x in range(0, len(s)) if x % 2 != 0]
    left.sort()
    right.sort()
    print(part1(left, right))
    print(part2(left, right))
