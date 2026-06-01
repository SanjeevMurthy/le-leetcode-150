from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         #nums1_length = m + n
#         # while len(nums1) < nums1_length:
#         #     nums1.append(0)
#         # print(nums1)
#         # print(len(nums1))
#         if len(nums1) > m:
#             nums1 = nums1[:m]
#             print("after stripping {}".format(nums1))
#             nums1.extend(nums2)
#             nums1.sort()
#             print(nums1)


# solu = Solution()
# solu.merge([1,2,3,0,0,0], 3,[2,5,6], 3)

# """
# [1,2,3,0,0,0]
# [2,5,6]
# [0, 0, 0, 2, 3, 5, 6]
# [1,2,3,0,0,0]

# [1,2,2,3,5,6]
# """


"""
Given an integer array nums, return true if any value appears atleast twice in the array, and return false if every element is distinct
"""

# Brute force approach
def check_duplicate_elements(nums: List[int]):
    # for i in nums:
        index_num = 0
        while index_num < len(nums):
            print("checking index num {}".format(index_num))
            new_nums = nums[index_num + 1:]
            print("new nums {}".format(new_nums))
            if nums[index_num] in new_nums:
                return True
            elif index_num == len(nums) - 1:
                return False
            else:
                index_num += 1

#hashset approach
def check_duplicate_elements_hashset(nums: List[int]):
    hash_set = set()
    for i in nums:
        if i not in hash_set:
            hash_set.add(i)
        else:
             print("for element {}".format(i))  
             return True
    return False    


nums = [1,2,3,4,5]
#status = check_duplicate_elements(nums)
#status = check_duplicate_elements_hashset(nums)
#print(status)
print("DONE")

hash_check = set()
try:
    hash_check.add(1)
    hash_check.add(2)
    hash_check.add(1)
except Exception as e:
     print(e)
print(hash_check)