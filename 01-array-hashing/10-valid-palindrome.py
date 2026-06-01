"""
### Valid Palindrome — Problem Statement
Given a string `s`, determine if it is a palindrome, considering only **alphanumeric characters** and **ignoring cases**.
A string is a palindrome if it reads the same forward and backward.

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string after removing non-alphanumeric characters.
```
### Constraints
* `1 ≤ s.length ≤ 2 × 10^5`
* `s` consists only of printable ASCII characters.

"""

def check_palindrome(text: str) -> bool :
    length = len(text)
    i =0 
    j = length - 1
    while i < j:
        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        else:
            if text[i].lower() != text[j].lower():
                return False
            else:
                i += 1
                j -= 1
    return True


s = "madaam"
print(check_palindrome(s))