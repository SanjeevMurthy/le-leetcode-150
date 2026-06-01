"""
Problem 9: +/- Queries Counting Pairs With Difference D (Q4)
Slot: Q4 | Probability: 5-10%

Maintain a multiset. Process a sequence of insert (+) and delete (-) operations.
After each operation, output the number of unordered pairs (a, b) in the current
multiset such that |a - b| == d.

Example (d=2):
    ops = [('+', 1), ('+', 3), ('+', 5), ('-', 3)]
    After +1: multiset={1},            pairs=0  -> output 0
    After +3: multiset={1,3},          pairs=1  (1,3) -> output 1
    After +5: multiset={1,3,5},        pairs=2  (1,3),(3,5) -> output 2
    After -3: multiset={1,5},          pairs=0  -> output 0

Key insight:
    When inserting value x, the new pairs created are (x, x+d) and (x, x-d),
    i.e. count[x+d] + count[x-d].
    When removing x, the pairs destroyed are the same count[x+d] + count[x-d]
    at the time AFTER the removal.

    Handle d=0 separately: a pair (x, x) requires at least 2 copies of x.
    Pairs = count[x] * (count[x]-1) / 2 for same-element pairs. But we track
    total pair count so we adjust incrementally.

Pattern: Hashmap counter under insert/delete.
LeetCode equivalents: 532 K-diff Pairs, 1814, 981 Time-Based Key-Value Store (design mindset)
"""

from collections import defaultdict


def solution(ops: list[tuple[str, int]], d: int) -> list[int]:
    """
    ops: list of ('+' | '-', value)
    d:   target absolute difference (>= 0)
    Returns list of pair counts after each operation.
    """
    count: dict[int, int] = defaultdict(int)
    pair_count = 0
    results = []

    for op, x in ops:
        if d == 0:
            # pairs = sum over all v of C(count[v], 2)
            # delta when inserting x: count[x] new pairs (before incrementing)
            # delta when removing  x: -(count[x]-1) pairs (before decrementing)
            if op == '+':
                pair_count += count[x]
                count[x] += 1
            else:
                count[x] -= 1
                pair_count -= count[x]
        else:
            if op == '+':
                pair_count += count[x + d] + count[x - d]
                count[x] += 1
            else:
                count[x] -= 1
                pair_count -= count[x + d] + count[x - d]

        results.append(pair_count)

    return results


# Variant: return only the final pair count
def count_pairs_with_diff(arr: list[int], d: int) -> int:
    count: dict[int, int] = defaultdict(int)
    for x in arr:
        count[x] += 1

    if d == 0:
        return sum(v * (v - 1) // 2 for v in count.values())

    result = 0
    for x in count:
        if x + d in count:
            result += count[x] * count[x + d]
    return result


if __name__ == "__main__":
    print("=== Incremental query tests ===")
    tests = [
        ([('+', 1), ('+', 3), ('+', 5), ('-', 3)], 2, [0, 1, 2, 0]),
        ([('+', 1), ('+', 1), ('+', 1)], 0, [0, 1, 3]),
        ([('+', 5), ('+', 5), ('-', 5)], 0, [0, 1, 0]),
        ([('+', 1), ('+', 4), ('+', 7), ('+', 10)], 3, [0, 1, 2, 3]),
        ([('+', 2), ('-', 2)], 5, [0, 0]),
    ]
    for ops, d, expected in tests:
        got = solution(ops, d)
        status = "PASS" if got == expected else "FAIL"
        print(f"[{status}] d={d}, ops={ops}")
        print(f"         got={got}  expected={expected}")

    print()
    print("=== Static array pair count tests ===")
    static_tests = [
        ([1, 3, 5, 7], 2, 3),
        ([1, 1, 1, 1], 0, 6),
        ([1, 2, 3, 4, 5], 1, 4),
        ([], 1, 0),
        ([5], 0, 0),
    ]
    for arr, d, expected in static_tests:
        got = count_pairs_with_diff(arr, d)
        status = "PASS" if got == expected else "FAIL"
        print(f"[{status}] arr={arr}, d={d} -> {got}  (expected {expected})")
