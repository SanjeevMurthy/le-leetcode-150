"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume:
Exactly one solution exists.
You cannot use the same element twice.

nums = [1,3,9,2,7,5]
target = 9

you can return the answer in any order
[3, 4]
"""

def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_hashmap(nums, target):
    hashmap = {}
    for i,num in enumerate(nums):
        complement = target - num
        print("for index [{}] and number {},  Checking for {}".format(i,num,complement))
        print("Current hashmap : {} \n ".format(hashmap))
        if complement in hashmap:
            print("Found {} in hashmap !!".format(complement))
            return [hashmap[complement], i]
        hashmap[num] = i
        
            
nums = [1,3,9,2,7,5]
target = 9
#print(two_sum_bruteforce(nums, target))
print(two_sum_hashmap(nums, target))