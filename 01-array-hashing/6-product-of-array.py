"""
Given an integer array nums, return an array answer such that:
answer[i] = product of all elements of nums except nums[i]
Example
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Constraints / Catch
You must solve it:
without division
in O(n) time
"""

def product_of_array_bf(nums):
    ans = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod = nums[j] * prod
        ans.append(prod)
    return ans

def product_of_array_optimal(nums):
    pre = 1
    post = 1
    ans = [1] * len(nums)
    for i, element in enumerate(nums):
        print("Checking for index {}".format(i))
        if i == 0:
            pre = pre * 1
            ans[i] = pre * nums[i]
            print("pre: {} \t ans[i]: {}".format(pre, ans[i]))
        else:
            pre = pre * nums[ i - 1]
            ans[i] = ans[i -1 ] * nums[ i - 1]
            print("pre: {} \t ans[i]: {}".format(pre, ans[i]))
    print(ans)
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) - 1:
            post = post * 1
            ans[i] = ans[i] * post
            print("post: {} \t ans[i]: {}".format(post, ans))
        else:
            post = post * nums[i + 1]
            ans[i] = ans[i] * post
            print("post: {} \t ans[i]: {}".format(post, ans))
    return ans


def product_of_array_good(nums):
    n = len(nums)
    ans = [1] * n

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]
        print("Index: {} \t Prefix: {} \t nums[i]: {} \t ans: {}".format(i,prefix,nums[i],ans))
    print(ans)
    postfix = 1
    for i in range(n-1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
        print("Index: {} \t Postfix: {} \t nums[i]: {} \t ans: {}".format(i,postfix,nums[i],ans))
    return ans


nums = [2,3,4,5] # [60, 40, 30, 24]
print("Product of an array {}".format(product_of_array_bf(nums)))
print("Product of an array OPTIMAL: {}".format(product_of_array_optimal(nums)))
print("Product of an array OPTIMAL: {}".format(product_of_array_good(nums)))