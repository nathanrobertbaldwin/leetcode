# Permutation in String

# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true

# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false

# Constraints:

#     1 <= s1.length, s2.length <= 1000


# Chars do not need to be in order, but need to be adjacent
# Would be nice to know what letters are in s1 in O(c)
# What about more than one letter? Use a freq counter.


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         charFreq = dict()

#         for c in s1:
#             charFreq[c] = 1 + charFreq.get(c, 0)

#         left = 0
#         right = 0
#         deltaCopy = charFreq.copy()

#         while right < len(s2):
#             removed = dict()
#             while right < len(s2) and s2[right] in deltaCopy or s2[right] in removed:
#                 if deltaCopy[s2[right]] > 0:
#                     deltaCopy[s2[right]] -= 1
#                     removed[s2[right]] = 1 + removed.get(s2[right], 0)

#                 if deltaCopy[s2[right]] == 0:
#                     if s2[right] in removed:
#                         left += 1
#                     del deltaCopy[s2[right]]

#                 if len(deltaCopy) == 0:
#                     return True
#                 right += 1

#             deltaCopy = charFreq.copy()
#             left = right
#             right += 1

#         return False


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         charFreq = dict()

#         for c in s1:
#             charFreq[c] = 1 + charFreq.get(c, 0)

#         left = 0
#         right = 0
#         deltaCopy = charFreq.copy()

#         while right < len(s2):

#             while right < len(s2) and s2[right] in deltaCopy:
#                 if s2[left] == s2[right]:
#                     left += 1
#                 else:
#                     deltaCopy[s2[right]] -= 1
#                     if deltaCopy[s2[right]] == 0:
#                         del deltaCopy[s2[right]]
#                 right += 1

#             if right - left - 1 == len(s1) and len(deltaCopy) == 0:
#                 return True

#             deltaCopy = charFreq.copy()
#             left += 1
#             right += 1

#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charFreq = dict()

        for c in s1:
            charFreq[c] = 1 + charFreq.get(c, 0)

        left = 0
        right = 0
        deltaCopy = charFreq.copy()

        while right < len(s2):
            while right < len(s2) and s2[right] in deltaCopy:
                deltaCopy[s2[right]] -= 1
                if deltaCopy[s2[right]] == 0:
                    del deltaCopy[s2[right]]
                right += 1

            if len(deltaCopy) == 0:
                return True

            deltaCopy = charFreq.copy()
            left += 1
            right = left

        return False


print(Solution.checkInclusion(None, s1="abc", s2="lecabee"))  # True
print(Solution.checkInclusion(None, s1="abc", s2="lecaabee"))  # False
print(Solution.checkInclusion(None, s1="adc", s2="dcda"))  # True
