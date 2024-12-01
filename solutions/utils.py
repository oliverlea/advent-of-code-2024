
from typing import List

def read_file(fn: str) -> List[str]:
    with open('./input/' + fn, 'r') as f:
        return f.readlines()