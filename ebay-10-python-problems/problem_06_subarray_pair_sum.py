"""
Problem 6: Subarray of Length m Containing a Pair Summing to k (Q3/Q4)
Slot: Q3 or Q4 | Probability: 8-15%

Given an array nums, a window size m, and a target k, count how many
contiguous subarrays of length exactly m contain at least one pair (i, j)
with i != j such that nums[i] + nums[j] == k.

Example:
    solution([1, 2, 3, 4, 5], 3, 5)
    Windows: [1,2,3] -> pairs: (2,3)=5 YES, (1,4)N, (1,2)N => count 1
             [2,3,4] -> pairs: (2,3)N,(2,4)N,(3,4)N,(1,4)N => NO...
             wait: (1,4) not in this window. pairs in [2,3,4]: none sum to 5
             [3,4,5] -> (1,4)N in window. Check: no pair sums to 5 in [3,4,5]... wait
             Actually pairs: (3,?): need 2, not in window. So 0?
             Hmm let me recount:
             [1,2,3]: 1+2=3, 1+3=4, 2+3=5 YES
             [2,3,4]: 2+3=5 YES
             [3,4,5]: 3+4=7, 3+5=8, 4+5=9 NO... wait again
             Actually let me try k=7: [3,4,5]: 3+4=7 YES

    solution([1, 2, 3, 4], 2, 5) -> 2
    Windows: [1,2]->3, [2,3]->5 YES, [3,4]->7 => 1?
    Actually [2,3]: 2+3=5 YES; [3,4]: 3+... wait, also only 2 elements so only one pair each.
    [1,2]=3 no, [2,3]=5 yes, [3,4]=7 no => count=1

Strategy:
    Slide a window of size m. Maintain a Counter of elements in the window.
    For each incoming element x, check if k-x is already in the window.
    If yes, there is at least one qualifying pair.

Time: O(n * m) worst case (inner loop over window elements) but amortised O(n)
      with the early-exit approach below.

Pattern: Sliding window + hashmap pair lookup.
LeetCode equivalents: LC 1 (Two Sum), 643/239 sliding window, 567, 2461
"""

from collections import defaultdict


def solution(nums: list[int], m: int, k: int) -> int:
    if m < 2 or len(nums) < m:
        return 0

    count = 0
    window: dict[int, int] = defaultdict(int)

    def _has_pair() -> bool:
        for x, freq in window.items():
            comp = k - x
            if comp in window:
                if comp != x:
                    return True
                if freq >= 2:   # same element used twice
                    return True
        return False

    # Build initial window
    for i in range(m):
        window[nums[i]] += 1

    if _has_pair():
        count += 1

    # Slide
    for i in range(m, len(nums)):
        # Add new element
        window[nums[i]] += 1
        # Remove outgoing element
        out = nums[i - m]
        window[out] -= 1
        if window[out] == 0:
            del window[out]

        if _has_pair():
            count += 1

    return count


# O(n) amortised version: track pair existence incrementally
def solution_incremental(nums: list[int], m: int, k: int) -> int:
    """
    Maintain pair_count = number of distinct unordered pairs in window summing to k.
    Increment/decrement as elements enter/leave.
    """
    if m < 2 or len(nums) < m:
        return 0

    window: dict[int, int] = defaultdict(int)
    pair_count = 0
    result = 0

    def _add(x: int) -> None:
        nonlocal pair_count
        comp = k - x
        if comp in window:
            # Adding x creates new pairs with every existing comp in window
            # But pair_count tracks whether >=1 pair exists, not the total count.
            # Track actual pair count for correctness.
            pair_count += window[comp]
        window[x] += 1

    def _remove(x: int) -> None:
        nonlocal pair_count
        window[x] -= 1
        if window[x] == 0:
            del window[x]
        comp = k - x
        if comp in window:
            pair_count -= window[comp]

    for i in range(m):
        _add(nums[i])

    result += 1 if pair_count > 0 else 0

    for i in range(m, len(nums)):
        _add(nums[i])
        _remove(nums[i - m])
        result += 1 if pair_count > 0 else 0

    return result


if __name__ == "__main__":
    tests = [
        # (nums, m, k, expected)
        ([1, 2, 3, 4], 2, 5, 1),      # [2,3] sums to 5
        ([1, 2, 3, 4, 5], 3, 5, 2),   # [1,2,3]->(2,3)=5, [2,3,4]->(2,3)=5
        ([1, 1, 1], 2, 2, 2),          # [1,1]->(1,1)=2 x2 windows
        ([1, 2, 3], 3, 10, 0),         # no pair sums to 10
        ([5, 5, 5, 5], 2, 10, 3),      # every window of size 2 has a pair
        ([1], 2, 2, 0),                # m > len
    ]
    for nums, m, k, expected in tests:
        got1 = solution(nums, m, k)
        got2 = solution_incremental(nums, m, k)
        ok = got1 == expected and got2 == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] nums={nums}, m={m}, k={k} -> {got1}/{got2}  (expected {expected})")
