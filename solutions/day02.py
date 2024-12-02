from typing import List
from utils import read_file

def verify_report(report: List[int]) -> bool:
    ascending = report[0] < report[1]
    if not ascending:
        report = report[::-1]
    return all(map(lambda x: x[0] < x[1] and x[1] - x[0] in {1, 2, 3}, zip(report, report[1:])))

def verify_report_tolerated(report: List[int]) -> bool:
    return any(verify_report(report[:x] + report[x + 1:]) for x in range(len(report)))

def verify(reports: List[List[int]], tolerate: bool = False) -> int:
    check = verify_report_tolerated if tolerate else verify_report
    result = 0
    for report in reports:
        if check(report):
            result += 1
    return result

def part2(reports: List[List[int]]) -> int:
    result = 0
    for report in reports:
        if verify_report_tolerated(report):
            result += 1
    return result

if __name__ == '__main__':
    lines = read_file('day02.txt')
    reports = [None] * len(lines)
    for i, line in enumerate(lines):
        reports[i] = [int(x) for x in line.split()]

    print(verify(reports))
    print(verify(reports, tolerate=True))