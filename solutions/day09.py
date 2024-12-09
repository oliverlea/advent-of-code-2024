
import heapq
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set
from utils import distance, read_file, within_bounds, Loc

def construct_disk(xs: List[int]) -> List[Optional[int]]:
    disk: List[Optional[int]] = [None] * sum(xs)
    cur = 0
    idee = 0
    for i in range(len(xs)):
        if i % 2 == 0:
            # writes
            for _ in range(xs[i]):
                disk[cur] = idee
                cur += 1
            idee += 1
        else:
            # frees
            for _ in range(xs[i]):
                cur += 1
    return disk

def checksum(disk: List[Optional[int]]) -> int:
    result = 0
    for i in range(len(disk)):
        cur = disk[i]
        if cur is not None:
            result += i * cur
    return result

def part1(xs: List[int]) -> int:
    disk = construct_disk(xs)
    left = 0
    while disk[left] is not None:
        left += 1
    right = len(disk) - 1
    while disk[right] is None:
        right -= 1
    while right > left:
        disk[left] = disk[right]
        disk[right] = None
        while disk[right] is None:
            right -= 1
        while disk[left] is not None:
            left += 1
    
    return checksum(disk)

def chunk_size(xs: List[Optional[int]], start: int, inc: int) -> int:
    cur = start
    chunk = 0
    while cur >= 0 and cur < len(xs) and xs[cur] == xs[start]:
        chunk += 1
        cur += inc
    return chunk

def part2(xs: List[int]) -> int:
    disk = construct_disk(xs)

    left = 0
    while disk[left] is not None:
        left += 1
    right = len(disk) - 1
    while disk[right] is None:
        right -= 1

    frees = defaultdict(list)
    i = 0
    while i < len(disk):
        if disk[i] is None:
            chunk = chunk_size(disk, i, 1)
            heapq.heappush(frees[chunk], i)
            i += chunk
        else:
            i += 1
    largest_free = max(frees.keys())

    i = len(disk) - 1
    while i >= 0:
        block = chunk_size(disk, i, -1)
        file_id = disk[i]
        if file_id is not None:
            earliest_free_index = None
            earliest_free_size = None
            for csize in range(block, largest_free + 1):
                if not frees[csize]:
                    continue
                lowest_index = frees[csize][0]
                if lowest_index < i:
                    if earliest_free_index is None or lowest_index < earliest_free_index:
                        earliest_free_index = lowest_index
                        earliest_free_size = csize
            if earliest_free_size:
                start_index = heapq.heappop(frees[earliest_free_size])
                for b in range(block):
                    disk[start_index + b] = disk[i - b]
                    disk[i - b] = None
                rem = earliest_free_size - block
                if rem:
                    heapq.heappush(frees[rem], start_index + block)
        i -= block
        while disk[i] is None:
            i -= 1

    return checksum(disk)
    
if __name__ == '__main__':
    xs = [int(x) for x in read_file('day09.txt')[0].strip()]
    print(part1(xs))
    print(part2(xs))