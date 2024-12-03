
import re
from typing import List
from utils import read_file

def part1(lines: List[str]) -> int:
    r = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0
    for line in lines:
        matches = r.findall(line)
        for left, right in matches:
            result += int(left) * int(right)
    return result


def part2(lines: List[str]) -> int:
    r = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    result = 0
    enabled = True
    for line in lines:
        matches = r.findall(line)
        for match in matches:
            group_matches = [x for x in match if x]
            if len(group_matches) == 3 and enabled:
                left, right = group_matches[1], group_matches[2]
                result += int(left) * int(right)
            elif len(group_matches) == 1:
                enabled = group_matches[0] == 'do()'
    return result

if __name__ == '__main__':
    lines = read_file('day03.txt')
    print(part1(lines))
    print(part2(lines))