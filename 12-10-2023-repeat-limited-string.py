# 2182. Construct String With Repeat Limit
# Medium
# Topics
# Companies
# Hint

# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

# Return the lexicographically largest repeatLimitedString possible.

# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.


# Example 1:

# Input: s = "cczazcc", repeatLimit = 3
# Output: "zzcccac"
# Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
# The letter 'a' appears at most 1 time in a row.
# The letter 'c' appears at most 3 times in a row.
# The letter 'z' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
# Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

from collections import Counter


def repeatLimitedString(s, repeatLimit):
    split = list(s)
    split.sort()

    left = len(split) - 1
    right = len(split)
    while len(split) > 0:



print(repeatLimitedString("cczazcc", 5))
