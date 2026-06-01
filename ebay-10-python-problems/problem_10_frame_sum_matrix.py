"""
Problem 10: Frame-Sum on Matrix / Maximum k×k Submatrix Sum + Unique-Element Sum (Q3)
Slot: Q3 | Probability: 4-8%

Two variants of this problem appear in reports:

Variant A — Maximum k×k submatrix sum:
    Given an n×m matrix and an integer k, find the maximum sum of any k×k submatrix.

Variant B — Maximum k×k submatrix sum counting only unique elements:
    Same as A, but within each k×k window, only include each distinct value once.

Both variants use a 2D prefix sum for Variant A.
Variant B requires a sliding-window with a set to track "first occurrence" of each value.

Example (Variant A):
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    k = 2
    Submatrices: top-left sums: 1+2+4+5=12, 2+3+5+6=16, 4+5+7+8=24, 5+6+8+9=28
    Answer: 28

Pattern: 2D prefix sum + set tracking of "touched" cells.
LeetCode equivalents: 1314 Matrix Block Sum, 304 Range Sum 2D, 221 Maximal Square
"""


def solution_max_submatrix_sum(matrix: list[list[int]], k: int) -> int:
    """Variant A: Maximum sum of any k×k submatrix. Time O(n*m), Space O(n*m)."""
    if not matrix or not matrix[0]:
        return 0
    n, m = len(matrix), len(matrix[0])
    if k > n or k > m:
        return 0

    # Build 2D prefix sum (1-indexed)
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (matrix[i - 1][j - 1]
                            + prefix[i - 1][j]
                            + prefix[i][j - 1]
                            - prefix[i - 1][j - 1])

    def rect_sum(r1: int, c1: int, r2: int, c2: int) -> int:
        # All 1-indexed, inclusive
        return (prefix[r2][c2]
                - prefix[r1 - 1][c2]
                - prefix[r2][c1 - 1]
                + prefix[r1 - 1][c1 - 1])

    max_sum = float('-inf')
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            s = rect_sum(i, j, i + k - 1, j + k - 1)
            if s > max_sum:
                max_sum = s

    return max_sum


def solution_max_submatrix_unique_sum(matrix: list[list[int]], k: int) -> int:
    """
    Variant B: Maximum sum counting only the FIRST occurrence of each value
    within each k×k window.
    Uses brute-force O(n * m * k^2) — acceptable for exam constraints (n,m <= 100).
    """
    if not matrix or not matrix[0]:
        return 0
    n, m = len(matrix), len(matrix[0])
    if k > n or k > m:
        return 0

    max_sum = float('-inf')
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            seen: set[int] = set()
            total = 0
            for r in range(i, i + k):
                for c in range(j, j + k):
                    v = matrix[r][c]
                    if v not in seen:
                        seen.add(v)
                        total += v
            if total > max_sum:
                max_sum = total

    return max_sum


def solution_all_submatrix_sums(matrix: list[list[int]], k: int) -> list[list[int]]:
    """
    Returns an n×m result matrix where result[i][j] is the sum of the k×k window
    centred at (i, j).  Cells where the window would extend outside are set to 0.
    (LC 1314 Matrix Block Sum style.)
    """
    if not matrix or not matrix[0]:
        return []
    n, m = len(matrix), len(matrix[0])

    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (matrix[i - 1][j - 1]
                            + prefix[i - 1][j]
                            + prefix[i][j - 1]
                            - prefix[i - 1][j - 1])

    def clamp_rect_sum(r1: int, c1: int, r2: int, c2: int) -> int:
        r1 = max(r1, 1)
        c1 = max(c1, 1)
        r2 = min(r2, n)
        c2 = min(c2, m)
        if r1 > r2 or c1 > c2:
            return 0
        return (prefix[r2][c2]
                - prefix[r1 - 1][c2]
                - prefix[r2][c1 - 1]
                + prefix[r1 - 1][c1 - 1])

    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = clamp_rect_sum(i + 1 - k, j + 1 - k, i + k, j + k)

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print("=== Variant A: Max k×k submatrix sum ===")
    a_tests = [
        (matrix, 2, 28),   # bottom-right 2x2: 5+6+8+9=28
        (matrix, 3, 45),   # full matrix sum
        (matrix, 1, 9),    # single cell max
        ([[1]], 1, 1),
        ([[1, 2], [3, 4]], 2, 10),
    ]
    for mat, k, expected in a_tests:
        got = solution_max_submatrix_sum(mat, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"  [{status}] k={k} -> {got}  (expected {expected})")

    print()
    print("=== Variant B: Max k×k unique-element sum ===")
    matrix2 = [
        [1, 1, 2],
        [1, 3, 2],
        [4, 1, 2],
    ]
    # k=2 windows unique sums:
    # [1,1,1,3] -> unique: {1,3} -> 4
    # [1,2,3,2] -> unique: {1,2,3} -> 6
    # [1,3,4,1] -> unique: {1,3,4} -> 8
    # [3,2,1,2] -> unique: {3,2,1} -> 6
    # best = 8
    b_tests = [
        (matrix2, 2, 8),
        ([[5, 5], [5, 5]], 2, 5),   # all same -> unique sum = 5
        (matrix, 2, 28),             # all distinct -> same as variant A
    ]
    for mat, k, expected in b_tests:
        got = solution_max_submatrix_unique_sum(mat, k)
        status = "PASS" if got == expected else "FAIL"
        print(f"  [{status}] k={k} -> {got}  (expected {expected})")

    print()
    print("=== Block sum (all windows centred) ===")
    mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"  matrix={mat3}, k=1 (each cell sums neighbourhood of radius 1):")
    result = solution_all_submatrix_sums(mat3, 1)
    for row in result:
        print(f"    {row}")
