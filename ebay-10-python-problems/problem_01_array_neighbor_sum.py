"""
Problem 1: Array Neighbor Sum / Sliding Triplet Sum (Q1)
Slot: Q1 (warm-up) | Probability: 35-50% (isomorph)

Given array a, return array b where:
    b[i] = a[i-1] + a[i] + a[i+1]
with 0-padding at boundaries.

Example: solution([4, 0, 1, -2, 3]) -> [4, 5, -1, 2, 1]
    b[0] = 0 + 4 + 0 = 4
    b[1] = 4 + 0 + 1 = 5
    b[2] = 0 + 1 + (-2) = -1
    b[3] = 1 + (-2) + 3 = 2
    b[4] = -2 + 3 + 0 = 1

Pattern: Array traversal + boundary handling.
LeetCode equivalents: 1652, 643, 1480
"""


def solution(a: list[int]) -> list[int]:
    n = len(a)
    b = []
    for i in range(n):
        left = a[i - 1] if i > 0 else 0
        right = a[i + 1] if i < n - 1 else 0
        b.append(left + a[i] + right)
    return b


# Generalised version: sum of k neighbours on each side
def solution_k_neighbors(a: list[int], k: int = 1) -> list[int]:
    n = len(a)
    result = []
    for i in range(n):
        total = sum(a[max(0, i - k): i + k + 1])
        result.append(total)
    return result


if __name__ == "__main__":
    tests = [
        ([4, 0, 1, -2, 3], [4, 5, -1, 2, 1]),
        ([1], [1]),
        ([1, 2], [3, 3]),
        ([1, 2, 3], [3, 6, 5]),
        ([-1, 0, 1], [-1, 0, 1]),
    ]
    for inp, expected in tests:
        got = solution(inp)
        status = "PASS" if got == expected else "FAIL"
        print(f"[{status}] solution({inp}) = {got}  (expected {expected})")
