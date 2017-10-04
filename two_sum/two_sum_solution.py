### Original problem posed by leetcode.com:
### Given an array of integers, return indices of the two numbers such that they add up to a specific target.
### You may assume that each input would have exactly one solution, and you may not use the same element twice.

### I've extended the solution to return pairs of indices corresponding to all possible solutions.



from itertools import combinations

def solution(array, target):
    combs = list(combinations(array, 2))
    sums = list(map(sum, combs))
    sums_location = [a for a, b in enumerate(sums) if b == target]
    integer_pairs = [combs[i] for i in sums_location]
    solution_indices = [(array.index(x), array.index(y)) for x, y in integer_pairs]
    return(solution_indices)
