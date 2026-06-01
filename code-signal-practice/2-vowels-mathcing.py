"""
Vowel-Consonant Pattern Matching (Easy/Medium)
Problem:
Given a binary pattern string (only 0 and 1) and a source string (lowercase letters), count how many substrings of source match the pattern, where:
0 in pattern means a vowel at that position
1 in pattern means a consonant at that position

Vowels are: a, e, i, o, u, y
Example:
pattern = "010", source = "amazing"

Output: 2
"010" matches "ama" (a-m-a: vowel-consonant-vowel) ✓
"010" matches "azi" (a-z-i: vowel-consonant-vowel) ✓
"010" doesn't match "maz", "zin", "ing"
"""

def vowel_consonant_matching(source, pattern):
    vowels = ["a", "e", "i", "o", "u"]
    source_list = list(source)
    pattern_length = len(pattern)
    matched_sub_str = []
    for i in range(len(source_list)):
        if i < len(source_list) - pattern_length + 1:
            sub_str = source_list[i:i+pattern_length]
            sub_str_pattern = ""
            for char in sub_str:
                if char in vowels:
                    sub_str_pattern += "0"
                else:
                    sub_str_pattern += "1"
            if sub_str_pattern == pattern:
                print("Checking substring:{} with pattern:{} \n".format(sub_str, sub_str_pattern))
                matched_sub_str.append(sub_str)
    return matched_sub_str
            #print("sub string: {}".format(sub_str))



pattern = "010"
source = "amazing"
print(vowel_consonant_matching(source, pattern))


# ─────────────────────────────────────────────
# Improved version — same logic, cleaner code
# Changes:
#   1. frozenset instead of list → O(1) membership lookup
#   2. 'y' added to vowels (per problem statement)
#   3. list(source) removed — strings are already sliceable
#   4. range bound set correctly — no inner guard clause needed
#   5. "".join() instead of += in a loop — avoids repeated string copies
#   6. encode() helper extracts the char → '0'/'1' concern
#   7. debug print removed from algorithm body
#   8. type hints + docstring added
# ─────────────────────────────────────────────

_VOWELS: frozenset[str] = frozenset("aeiouy")


def _encode(char: str) -> str:
    """Return '0' if char is a vowel, '1' if consonant."""
    return "0" if char in _VOWELS else "1"


def vowel_consonant_matching_v2(source: str, pattern: str) -> list[str]:
    pattern_length = len(pattern)
    matched: list[str] = []

    for i in range(len(source) - pattern_length + 1):
        sub_str = source[i : i + pattern_length]
        sub_str_pattern = "".join(_encode(c) for c in sub_str)
        if sub_str_pattern == pattern:
            matched.append(sub_str)

    return matched


# ── comparison run ──
print("v1:", vowel_consonant_matching(source, pattern))
print("v2:", vowel_consonant_matching_v2(source, pattern))