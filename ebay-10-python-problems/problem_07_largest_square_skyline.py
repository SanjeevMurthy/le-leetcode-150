"""
Problem 7: Largest Square in Skyline / Histogram Square (Q4)
Slot: Q4 | Probability: 5-12%

Given an array `buildings` where buildings[i] is the height of building i
(each building has width 1), find the side length of the largest square
that fits entirely within the skyline histogram.

A k×k square starting at column i requires:
    min(buildings[i], buildings[i+1], ..., buildings[i+k-1]) >= k

Example:
    buildings = [3, 2, 4, 1, 5, 2]
    Largest square: side 2 (fits at index 0-1 with min height 2, or 4-5 with min 2)
    side 3: columns 0-2 -> min(3,2,4)=2 < 3, no. columns 2-4 -> min(4,1,5)=1 <3, no.
    Answer: 2

Strategy A (O(n²) — safe under exam pressure):
    For every starting column i, track the running min as you extend right.
    The largest possible square from column i to j has side = min(min_height, width).

Strategy B (O(n log n) — monotonic stack / sparse table for prefix-min queries):
    Precompute sparse table for range-min queries in O(1).
    Binary search on side length for each starting column.

Pattern: Monotonic stack or O(n²) brute-force on prefix-min arrays.
LeetCode equivalents: 84 Largest Rectangle in Histogram, 221 Maximal Square, 85
"""

import math


def solution(buildings: list[int]) -> int:
    n = len(buildings)
    if n == 0:
        return 0

    max_side = 0
    for i in range(n):
        min_h = buildings[i]
        for j in range(i, n):
            min_h = min(min_h, buildings[j])
            width = j - i + 1
            side = min(min_h, width)
            if side > max_side:
                max_side = side

    return max_side


# O(n log n) approach using sparse table for range-min queries
class SparseTable:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        k = max(1, n.bit_length())
        self.table = [[0] * n for _ in range(k)]
        self.table[0] = arr[:]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j - 1][i],
                                       self.table[j - 1][i + (1 << (j - 1))])

    def query(self, l: int, r: int) -> int:
        length = r - l + 1
        k = length.bit_length() - 1
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])


def solution_optimized(buildings: list[int]) -> int:
    n = len(buildings)
    if n == 0:
        return 0

    st = SparseTable(buildings)
    max_side = 0

    for i in range(n):
        # Binary search: find the largest side s such that
        # min(buildings[i..i+s-1]) >= s
        lo, hi = 1, min(buildings[i], n - i)
        while lo <= hi:
            mid = (lo + hi) // 2
            if st.query(i, i + mid - 1) >= mid:
                max_side = max(max_side, mid)
                lo = mid + 1
            else:
                hi = mid - 1

    return max_side


if __name__ == "__main__":
    tests = [
        ([3, 2, 4, 1, 5, 2], 2),
        ([4, 4, 4, 4], 4),
        ([1, 2, 3, 4], 2),
        ([4, 3, 2, 1], 2),
        ([5], 1),
        ([1, 1, 1, 1, 1], 1),    # heights=1, so side=min(1,width)=1 regardless of width
        ([2, 2, 2], 2),           # width=2->min=2->side=2; width=3->min=2->side=2
        ([3, 3, 3], 3),
        ([], 0),
        ([5, 5, 1, 5, 5], 2),
    ]
    for b, expected in tests:
        got = solution(b)
        got_opt = solution_optimized(b) if b else 0
        ok = got == expected and got_opt == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {b} -> brute={got}, optimised={got_opt}  (expected {expected})")
