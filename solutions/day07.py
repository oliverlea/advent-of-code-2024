
from typing import List, Tuple
from utils import read_file

OPS = [
    lambda x, y: x + y,
    lambda x, y: x * y,
    lambda x, y: int(f"{x}{y}")
]

def parse(line: str) -> Tuple[int, List[int]]:
    target, remainder = line.split(":")
    values = [int(x) for x in remainder.strip().split(" ")]
    return int(target), values

def solve(xs: List[Tuple[int, List[int]]], ops) -> int:
    def rsolve(target: int, inputs: List[int], cur_sum: int) -> int:
        if not inputs:
            return target if cur_sum == target else 0
        for op in ops:
            if (r := op(cur_sum, inputs[0])) <= target and rsolve(target, inputs[1:], r):
                return target
        return 0
    return sum(rsolve(target, inputs, 0) for target, inputs in xs)

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day07.txt')]
    xs: List[Tuple[int, List[int]]] = [parse(line) for line in lines]
    print(solve(xs, OPS[0:2]))
    print(solve(xs, OPS))