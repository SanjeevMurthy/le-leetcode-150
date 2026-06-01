"""
Problem 8: Black/White Checkerboard Matrix Queries (Q3)
Slot: Q3 | Probability: 5-10%

Given an n×m matrix and a list of queries, each query asks for the k-th smallest
element among cells of a specific color (black or white), where a cell at (i, j) is:
    black  if (i + j) is even
    white  if (i + j) is odd

After each query the cell containing the k-th smallest element has its value
updated (set to 0, or replaced) — the exact mutation depends on the variant.

The version below: no mutation; just answer each (color, k) query.
Variant with mutation is also included.

Example:
    matrix = [[1, 2], [3, 4]]
    Black cells (i+j even): (0,0)=1, (1,1)=4  -> sorted [1, 4]
    White cells (i+j odd):  (0,1)=2, (1,0)=3  -> sorted [2, 3]
    query("black", 1) -> 1
    query("white", 2) -> 3

Strategy:
    Separate black and white cells into two sorted lists.
    Use bisect for O(log n) lookup after any mutations.

Pattern: Classification + sorted selection + optional update.
LeetCode equivalents: 2616, 378 Kth Smallest in Sorted Matrix, 2089
"""

import bisect


def solution(matrix: list[list[int]], queries: list[tuple]) -> list[int]:
    """
    queries: list of (color, k) where color in {"black", "white"}, k is 1-indexed.
    Returns a list of answers.
    """
    n = len(matrix)
    m = len(matrix[0])

    black = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 0)
    white = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 1)

    results = []
    for color, k in queries:
        arr = black if color == "black" else white
        results.append(arr[k - 1])
    return results


def solution_with_mutation(matrix: list[list[int]], queries: list[tuple]) -> list[int]:
    """
    Each query: (color, k) -> find k-th smallest among that color's cells,
    record its value, then set that cell to 0 (mutation).
    Returns list of the recorded values.
    """
    n = len(matrix)
    m = len(matrix[0])

    # Store as sorted lists; each element is the value (we rebuild after mutation)
    black = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 0)
    white = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 1)

    results = []
    for color, k in queries:
        arr = black if color == "black" else white
        val = arr[k - 1]
        results.append(val)
        # Remove the found element and insert 0
        arr.pop(k - 1)
        bisect.insort(arr, 0)

    return results


def solution_with_average_query(matrix: list[list[int]], queries: list[tuple]) -> list[float]:
    """
    Variant: each query (color, k) returns the AVERAGE of the k smallest
    elements of that color (no mutation).
    """
    n = len(matrix)
    m = len(matrix[0])

    black = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 0)
    white = sorted(matrix[i][j] for i in range(n) for j in range(m) if (i + j) % 2 == 1)

    results = []
    for color, k in queries:
        arr = black if color == "black" else white
        results.append(sum(arr[:k]) / k)
    return results


if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    # black cells: (0,0)=1, (1,1)=4  -> [1,4]
    # white cells: (0,1)=2, (1,0)=3  -> [2,3]

    tests_basic = [
        (matrix1, [("black", 1), ("black", 2), ("white", 1), ("white", 2)], [1, 4, 2, 3]),
    ]
    for mat, qs, expected in tests_basic:
        got = solution(mat, qs)
        status = "PASS" if got == expected else "FAIL"
        print(f"[{status}] solution queries={qs} -> {got}  (expected {expected})")

    print()

    matrix2 = [[5, 1, 3], [2, 8, 4], [7, 6, 9]]
    # black (i+j even): (0,0)=5,(0,2)=3,(1,1)=8,(2,0)=7,(2,2)=9 -> sorted [3,5,7,8,9]
    # white (i+j odd):  (0,1)=1,(1,0)=2,(1,2)=4,(2,1)=6        -> sorted [1,2,4,6]
    queries2 = [("black", 3), ("white", 2), ("black", 1)]
    expected2 = [7, 2, 3]
    got2 = solution(matrix2, queries2)
    status = "PASS" if got2 == expected2 else "FAIL"
    print(f"[{status}] matrix2 queries -> {got2}  (expected {expected2})")

    print()
    print("Mutation variant:")
    mat3 = [[3, 1], [2, 4]]
    # black: [3,4], white: [1,2]
    qs3 = [("black", 1), ("black", 1)]
    # query1: black 1st smallest = 3, set to 0 -> black=[0,4]
    # query2: black 1st smallest = 0
    got3 = solution_with_mutation(mat3, qs3)
    print(f"  mutation result: {got3}  (expected [3, 0])")
    assert got3 == [3, 0], f"FAIL: {got3}"
    print("  PASS")
