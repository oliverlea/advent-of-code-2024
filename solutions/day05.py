
from collections import defaultdict
from functools import cmp_to_key
from typing import Dict, List, Set
from utils import read_file

def construct_before(lines: List[str]) -> Dict[int, Set[int]]:
    before: Dict[int, Set[int]] = defaultdict(set)
    for line in lines:
        if not line:
            break
        s = line.split("|")
        target = int(s[0])
        right = int(s[1])
        before[target].add(right)
    return before

def valid(ordering: List[int], before: Dict[int, Set[int]]) -> bool:
    seen: Set[int] = set()
    for x in ordering:
        for b in before[x]:
            if b in seen:
                return False
        seen.add(x)
    return True

def part1(lines: List[str]) -> int:
    before = construct_before(lines)
    
    index = 0
    while lines[index]:
        index += 1
    index += 1

    result = 0
    while index < len(lines):
        line = lines[index]
        page_ordering = [int(x) for x in line.split(",")]
        if valid(page_ordering, before):
            result += page_ordering[len(page_ordering) // 2]
        index += 1
    return result


def part2(lines: List[str]) -> int:
    before = construct_before(lines)
    index = 0
    while lines[index]:
        index += 1
    index += 1

    invalid: List[List[int]] = []
    while index < len(lines):
        line = lines[index]
        page_ordering = [int(x) for x in line.split(",")]
        if not valid(page_ordering, before):
            invalid.append(page_ordering)
        index += 1

    def compare(x: int, y: int) -> int:
        if y in before[x]:
            return 1
        return -1
    
    result = 0
    for inv in invalid:
        list_result = sorted(inv, key=cmp_to_key(compare))
        result += list_result[len(list_result) // 2]
    return result

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day05.txt')]
    print(part1(lines))
    print(part2(lines))