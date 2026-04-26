from typing import List, Any, Dict, Tuple, Generator

def sieve_of_eratosthenes(n: int) -> List[int]:
    if n <= 2:
        return []
    nums = list(range(2, n))
    for i in nums:
        nums = [x for x in nums if x == i or x % i != 0]
    return nums

def triple_combinations(lst: List[int]) -> List[Tuple[int, int, int]]:
    return [(lst[i], lst[j], lst[k])
            for i in range(len(lst))
            for j in range(i+1, len(lst))
            for k in range(j+1, len(lst))]

def dict_table(n: int) -> Dict[int, Dict[int, int]]:
    return {i: {j: i*j for j in range(1, n+1)} for i in range(1, n+1)}

def generators(n: int) -> Generator[Generator[int, None, None], None, None]:
    for _ in range(n):
        yield (i for i in range(1, n+1))

def cartesian_product(set_a: List[Any], set_b: List[Any]) -> List[Tuple[Any, Any]]:
    return [(a, b) for a in set_a for b in set_b]