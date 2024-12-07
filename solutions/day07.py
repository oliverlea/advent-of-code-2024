
from typing import List, Tuple
from utils import read_file

OPS = [
    lambda x, y: x + y,
    lambda x, y: x * y,
    lambda x, y: int(str(x) + str(y)),
]

def parse(line: str) -> Tuple[int, List[int]]:
    target, remainder = line.split(":")
    values = [int(x) for x in remainder.strip().split(" ")]
    return int(target), values

def solve(xs: List[Tuple[int, List[int]]], ops) -> int:
    def solvable(target: int, inputs: List[int], cur_sum: int) -> bool:
        if not inputs:
            return cur_sum == target
        n = inputs[0]
        return any(solvable(target, inputs[1:], op(cur_sum, n)) for op in ops)

    return sum(target for target, inputs in xs if solvable(target, inputs, 0))

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day07.txt')]
    xs: List[Tuple[int, List[int]]] = [parse(line) for line in lines]
    print(solve(xs, OPS[0:2]))
    print(solve(xs, OPS))