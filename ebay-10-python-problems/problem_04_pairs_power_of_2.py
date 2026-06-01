"""
Problem 4: Pairs Whose Sum is a Power of 2 (Q4)
Slot: Q4 | Probability: 20-35% (isomorph)

Given an array of integers, count the number of pairs (i, j) with i < j
such that a[i] + a[j] is a power of 2 (1, 2, 4, 8, 16, ...).

Example:
    solution([1, 1, 2, 2]) -> 2
    Pairs: (1,1)->2=2^1 MATCH, (1,2)->3 no, (1,2)->3 no,
           (1,2)->3 no, (1,2)->3 no, (2,2)->4=2^2 MATCH  -> 2

Strategy:
    For each unique value v, iterate over all powers of 2 p.
    The complement is p - v. Use a Counter to look up pair counts.
    To avoid double-counting, only process pairs where complement >= v
    (if equal, use n*(n-1)//2 for same-element pairs).

Time: O(n * log(max_val))  Space: O(n)

Pattern: Hashmap counter + iterate over small target set.
LeetCode equivalents: 1 Two Sum, 532 K-diff Pairs, 1865, 1814, 1010
"""

from collections import Counter


def _is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def solution(a: list[int]) -> int:
    if not a:
        return 0

    count = Counter(a)
    max_val = max(a)
    result = 0

    for v in list(count.keys()):
        p = 1
        while p <= 2 * max_val:  # upper bound: largest possible sum
            complement = p - v
            if complement in count:
                if complement > v:
                    result += count[v] * count[complement]
                elif complement == v:
                    result += count[v] * (count[v] - 1) // 2
                # complement < v: already counted when v was the smaller element
            p <<= 1  # next power of 2

    return result


# Brute force O(n^2) — useful as backup for partial credit under time pressure
def solution_brute(a: list[int]) -> int:
    n = len(a)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            if s > 0 and _is_power_of_two(s):
                result += 1
    return result


if __name__ == "__main__":
    tests = [
        ([1, 1, 2, 2], 2),          # (1,1)=2, (2,2)=4
        ([1, 5, 3, 1, 3], 7),       # (1,3)x3, (1,1)=2, (5,3)x2=8, (3,1)=4 -> 7
        ([2, 2, 2, 2], 6),          # all 4-choose-2 pairs sum to 4
        ([1], 0),
        ([], 0),
        ([7, 1], 1),                 # 7+1=8
        ([3, 5, 1, 7], 3),          # (3,5)=8, (3,1)=4, (1,7)=8
        ([1, 3, 5, 7, 9, 15], 5),   # (1,3)=4,(1,7)=8,(1,15)=16,(3,5)=8,(7,9)=16
    ]
    for a, expected in tests:
        got = solution(a)
        brute = solution_brute(a)
        ok_main = got == expected
        ok_brute = brute == expected
        status = "PASS" if ok_main and ok_brute else "FAIL"
        print(f"[{status}] a={a} -> optimised={got}, brute={brute}  (expected {expected})")
