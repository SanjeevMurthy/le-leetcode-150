"""
### Two Sum II - Input Array Is Sorted — Problem Statement
Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific target number.
Let these two numbers be `numbers[index1]` and `numbers[index2]` where
`1 ≤ index1 < index2 ≤ numbers.length`.
Return the indices of the two numbers, `index1` and `index2`, **added by one as a 1-indexed array** `[index1, index2]`.

You may assume that:
* Each input has **exactly one solution**
* You may **not use the same element twice**
* Your solution must use **only constant extra space**

---
**Example 1:**
```python
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9
```
---
**Example 2:**
```python
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: 2 + 4 = 6
```
---
### Constraints
* `2 ≤ numbers.length ≤ 3 × 10^4`
* `-1000 ≤ numbers[i] ≤ 1000`
* `numbers` is sorted in non-decreasing order
* `-1000 ≤ target ≤ 1000`
* Exactly one solution exists
"""
from collections import defaultdict

def two_sum_pointer(nums, target):
    length = len(nums)
    left_pointer = 0
    right_pointer = length -1
    while left_pointer < right_pointer:
        if nums[left_pointer]+ nums[right_pointer] > target:
            right_pointer -= 1
        elif nums[left_pointer] + nums[right_pointer] < target:
            left_pointer += 1
        elif nums[left_pointer] + nums[right_pointer] == target:
            return [left_pointer+1, right_pointer+1]
        else:
            return None
        
def two_sum_hashmap(nums, target):
    hash_map = defaultdict(list)
    for i, num in enumerate(nums):
        comp = target - num
        print("Existing Hashmap: {}".format(hash_map))
        print("Checking for index {} and num: {} for complement: {}".format(i,num, comp))
        if comp in hash_map:
            print("Found complement !! {}".format(comp))
            return [hash_map[comp]+1, i+1]
        else:
            hash_map[num] = i


numbers = [2,7,11,15]
target = 9
#print(two_sum_pointer(numbers, target))
print(two_sum_hashmap(numbers, target))