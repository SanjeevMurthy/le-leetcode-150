"""
### 3Sum — Problem Statement
Given an integer array `nums`, return **all the triplets** `[nums[i], nums[j], nums[k]]` such that:
* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`
---
### Requirements
* The solution set must **not contain duplicate triplets**
* You can return the answer in **any order**
---
**Example 1:**
```python
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
Distinct triplets are [-1,0,1] and [-1,-1,2]
```
---
**Example 2:**
```python
Input: nums = [0,1,1]
Output: []
Explanation: No triplets sum to 0
```
---
**Example 3:**
```python
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: Only one valid triplet exists
```
---
### Constraints
* `3 ≤ nums.length ≤ 3000`
* `-10^5 ≤ nums[i] ≤ 10^5`
"""

# def two_sum_pointer(nums, target):
#     length = len(nums)
#     left_pointer = 0
#     right_pointer = length -1
#     while left_pointer < right_pointer:
#         if nums[left_pointer]+ nums[right_pointer] > target:
#             right_pointer -= 1
#         elif nums[left_pointer] + nums[right_pointer] < target:
#             left_pointer += 1
#         elif nums[left_pointer] + nums[right_pointer] == target:
#             return [left_pointer+1, right_pointer+1]
#         else:
#             return None

def three_sum_pointer(nums):
    length = len(nums)
    sorted_nums = sorted(nums)
    ans_list = []
    for i in range(length-2):
        # skip duplicates for i
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
            continue
        # optimization: stop if number > 0
        if sorted_nums[i] > 0:
            break
        lh_index = i + 1
        rh_index = length - 1
        
        while lh_index < rh_index:
            total = sorted_nums[i]+sorted_nums[lh_index]+sorted_nums[rh_index]

            if total < 0:
                lh_index += 1
            elif total > 0:
                rh_index -= 1
            else:
                ans_list.append([sorted_nums[i],sorted_nums[lh_index],sorted_nums[rh_index]])
                while lh_index < rh_index and sorted_nums[lh_index] == sorted_nums[lh_index+1]:
                    lh_index += 1
                while lh_index < rh_index and sorted_nums[rh_index] == sorted_nums[rh_index-1]:
                    rh_index -= 1
                lh_index += 1
                rh_index -= 1
    return ans_list



nums = [-1,0,1,2,-1,-4]
print(three_sum_pointer(nums))