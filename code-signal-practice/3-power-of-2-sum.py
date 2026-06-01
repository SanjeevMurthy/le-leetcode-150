"""
Pairs Summing to Powers of 2 (Hard — Hashmap)
Problem:
Given an array of unique integers numbers, count pairs of indices (i, j) where i ≤ j and numbers[i] + numbers[j] equals some power of 2 (i.e., 1, 2, 4, 8, ...).

Example:

numbers = [1, -1, 2, 3]
Output: 5

Sum = 1: (1,2) → -1 + 2 = 1
Sum = 2: (0,0) → 1 + 1; (1,3) → -1 + 3
Sum = 4: (0,3) → 1 + 3; (2,2) → 2 + 2
Total: 5 pairs
Constraints: n ≤ 10^5, |numbers[i]| ≤ 10^6. Naive O(n²) = 10^10 → times out. Need O(n × log(max)).
"""


def solution(numbers):
    seen = set(numbers)
    powers = set([1 << i for i in range(22)])
    count = 0
    print(seen)
    print(powers)
    for x in numbers:
        for p in powers:
            y = p - x
            if y in seen:
                print("x:{}\t y:{} \t power:{}\t".format(x,y,p))
                if y >= x:
                    count += 1
    return count


numbers = [1, -1, 2, 3]
print(solution(numbers))