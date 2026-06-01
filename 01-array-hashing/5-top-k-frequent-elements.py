"""
Given an integer array nums and an integer k, return the k most frequent elements.

Example:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""
from collections import Counter
import heapq

def top_k_frequent_elements(nums, k):
    hash_map = {}
    for i in nums:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    print(hash_map)
    sorted_list = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    top_k_with_occurance = sorted_list[:k]
    print(top_k_with_occurance)
    top_k_elements = []
    for num, occurance in top_k_with_occurance:
        top_k_elements.append(num)
    return top_k_elements

def top_k_counter(nums, k):
    c = Counter(nums)
    freq_elements = c.most_common(k)
    return [num for num, freq in freq_elements]

def top_k_freq_elements_priorityqueue(nums,k):
    freq_map = Counter(nums)
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq, num in min_heap]


nums = [1,1,1,2,2,2,3,4,6,6,8,6,9]
k = 4
topk = top_k_frequent_elements(nums, k)
print("Top elements in the list {}".format(topk))
print("Top elements in the list using counter:  {}".format(top_k_counter(nums,k)))
print("Top elements in the list using heap(priority queue):  {}".format(top_k_freq_elements_priorityqueue(nums,k)))