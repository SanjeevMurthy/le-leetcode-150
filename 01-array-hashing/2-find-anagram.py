#given 2 strings s and t, return true if t is an anagram of s, and false otherwise

"""
Will check the len of the the string, if they are not equal they cannot be anagrams.
Then will initialize an array for 26 alphabets based on the ascii value of the character
from list S, for each of the char, will increment its position from char_Set
from list t, for each of the char, will decrement the value by one in its position from char_set
"""

s = "sanju"
t = "januj"
char_set = [0] * 26

def check_anagram(s, t):
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            print("iteration {}".format(i))
            char_set[ord(s[i]) - ord('a')] += 1
            char_set[ord(t[i]) - ord('a')] -= 1
            print(char_set)
            print("\n")
        for i in char_set:
            if i != 0:
                print("value {} for character {}".format(i, chr(char_set.index(i) + ord('a'))))
                print("Returning False")
                return False
            # else:
            #     continue
        return True
    


if check_anagram(s,t):
    print("Strings are anagram")
else:
    print("Strings are not anagram")