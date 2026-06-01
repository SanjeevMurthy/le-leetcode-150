"""
Array Neighbor Sum (Easy)
Problem:
Given an array a, return an array b of the same length where each element b[i] = a[i-1] + a[i] + a[i+1]. If a[i-1] or a[i+1] doesn't exist (out of bounds), use 0 in its place.

Example:

Input:  a = [4, 0, 1, -2, 3]
Output: b = [4, 5, -1, 2, 1]

b[0] = 0 + 4 + 0 = 4         (no left neighbor)
b[1] = 4 + 0 + 1 = 5
b[2] = 0 + 1 + (-2) = -1
b[3] = 1 + (-2) + 3 = 2
b[4] = (-2) + 3 + 0 = 1      (no right neighbor)
"""

def neighbor_sum(a):
    b=[0] * len(a)
    for i in range(len(a)):
        if i - 1 < 0 and i < len(a):
            LN = 0
            nsum = LN + a[i] + a[i+1]
            b[i] = nsum
        elif i + 1 >= len(a):
            RN = 0
            nsum = a[i-1] + a[i] + RN
            b[i] = nsum
        else:
            nsum = a[i-1] + a[i] + a[i+1]
            b[i] = nsum
    return b

def neighbor_sum_better(a):
    n = len(a)
    return [
        (a[i-1] if i > 0 else 0) + a[i] + (a[i+1] if i < n-1 else 0) for i in range(n)
    ]

def list_comprehension(a):
    return [(a[i] * a[i]) for i in range(len(a))]

a = [4, 0, 1, -2, 3]
print(neighbor_sum(a))
print(neighbor_sum_better(a))
print(list_comprehension(a))