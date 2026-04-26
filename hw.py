from typing import List, Any, Dict, Set, Generator

def squares(n: int):
    return [i**2 for i in range(n+1)]

def unique_squares(numbers: List[int]) -> Set[int]:
    return {x**2 for x in set(numbers)}

def char_counts(text: str) -> Dict[str, int]:
    return {c: text.count(c) for c in set(text)}

def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]

def squares_gen(n: int) -> Generator[int, None, None]:
    return (i**2 for i in range(n+1))

def odd_squares(n: int) -> set[int]:
    return {i**2 for i in range(1, n+1, 2)}

def index_map(text: str) -> dict[str, int]:
    return {c: i for i, c in enumerate(text)}

def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {item for sub in nested_list for item in sub}

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    def gen():
        a, b = 0, 1
        yield a
        yield b
        for _ in range(2, n):
            a, b = b, a + b
            yield b
    return gen()

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {v: k for k, v in d.items()}

def primes(n: int) -> List[int]:
    return [i for i in range(2, n+1) if all(i % x != 0 for x in range(2, int(i**0.5)+1))]

def intersection(sets: List[Set[Any]]) -> Set[Any]:
    if not sets:
        return set()
    return {x for x in sets[0] if all(x in s for s in sets)}

def factorials_gen(n: int) -> Generator[int, None, None]:
    import math
    return (math.factorial(i) for i in range(n))

def str_lengths(strings: List[str]) -> Dict[str, int]:
    return {s: len(s) for s in strings}

def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    return (lst[i] for i in range(len(lst)-1, -1, -1))

def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    return {l: [w for w in words if len(w) == l] for l in set(map(len, words))}

def common_elements(lists: List[List[Any]]) -> Set[Any]:
    if not lists:
        return set()
    return {x for x in lists[0] if all(x in lst for lst in lists)}

def primes_gen(n: int) -> Generator[int, None, None]:
    return (i for i in range(2, n+1) if all(i % x != 0 for x in range(2, int(i**0.5)+1)))

def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: v for i, v in enumerate(lst)}