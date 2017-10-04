
from itertools import combinations

def solution(array, target):
    combs = list(combinations(array, 2))
    sums = list(map(sum, combs))
    sums_location = [a for a, b in enumerate(sums) if b == target]
    integer_pairs = [combs[i] for i in sums_location]
    solution_indices = [(array.index(x), array.index(y)) for x, y in integer_pairs]
    return(solution_indices)
