"""
Given an array of strings strs, group the anagrams together.
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output:
[
 ["eat","tea","ate"],
 ["tan","nat"],
 ["bat"]
]

Two words are anagrams if they contain the same letters with same frequency, just rearranged.


Approach:
Generate the hash string (char set with 1 for the ascii position of the string) for each of the string in array - and try to add it as a key to the hasmap, along with the original string as the value
"""

from collections import defaultdict

def get_anagrams_group(string_list):
    hash_map = defaultdict(list)
    for each_string in string_list:
        print(each_string)
        char_set = [0] * 26
        for char in each_string:
            char_set[ord(char) - ord('a')] += 1
        print(char_set)
        hash_key = tuple(char_set)
        hash_map[hash_key].append(each_string)
    print(hash_map)
    return list(hash_map.values())


def get_anagrams_group_by_sort(string_list):
    groups = defaultdict(list)
    for w in string_list:
        key = ''.join(sorted(w))
        groups[key].append(w)
    print(groups)
    return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
ag = get_anagrams_group(strs)
print("Anagrams group \n {}".format(ag))


ag = get_anagrams_group_by_sort(strs)
print("Anagrams group by sort \n {}".format(ag))
