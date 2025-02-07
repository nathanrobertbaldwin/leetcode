# Longest Repeating Character Replacement

# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4

# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5

# Solution Issue: This algorithm finds the longest substring where all substitutions are made either at the
# beginning or end of the string. It does not find the longest substring when some number of substitutions are
# made at the beginning, and some are made at the end.

# class Solution:

#     def examine(self, s: str, k: int):
#         longest = 1
#         slow = 0
#         fast = 1
#         count = 0

#         while fast < len(s):
#             while fast < len(s) and (s[slow] == s[fast] or count < k):
#                 if s[slow] == s[fast]:
#                     fast += 1
#                 else:
#                     count += 1
#                     fast += 1

#             longest = max(longest, fast - slow)

#             slow = fast - count
#             fast = slow + 1
#             count = 0

#         longest = max(longest, fast - slow)
#         return longest

#     def characterReplacement(self, s: str, k: int) -> int:

#         longest_right = Solution.examine(None, s, k)
#         longest_left = Solution.examine(None, s[::-1], k)
#         return max(longest_right, longest_left)

# Since k could be 0, count < k shouldn't be a controller of the function.

# class Solution:
#     def characterReplacement(self, s: str, k: int):
#         longest = 1
#         slow = 0
#         fast = 1
#         count = 0

#         while fast < len(s):
#             new_slow = 0
#             while fast < len(s) and (s[slow] == s[fast] or count < k):
#                 if s[slow] != s[fast]:
#                     if new_slow == 0:
#                         new_slow = fast
#                     count += 1
#                 fast += 1

#             if count < k:
#                 t_slow = slow
#                 while slow > 0 and (s[slow] != s[t_slow] or count < k):
#                     if s[slow] != s[t_slow]:
#                         count += 1
#                     slow -= 1

#             longest = max(longest, fast - slow)

#             if new_slow > 0: # HOW CAN I MAKE THIS WORK?
#                 slow = new_slow

#             fast = slow + 1
#             count = 0

#         longest = max(longest, fast - slow)
#         return longest


class Solution:
    def characterReplacement(self, s: str, k: int):
        left = 0
        counter = dict()
        maxF = 0
        longest = 0
        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            maxF = max(maxF, counter[s[right]])
            while (right - left + 1) - maxF > k:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest


print(Solution.characterReplacement(None, s="XYYX", k=2))  # 4
print(Solution.characterReplacement(None, s="AAABABB", k=1))  # 5
print(Solution.characterReplacement(None, s="AAAA", k=2))  # 4
print(Solution.characterReplacement(None, s="ABCDE", k=1))  # 2
print(Solution.characterReplacement(None, s="BAAAB", k=2))  # 5
print(Solution.characterReplacement(None, s="ABAA", k=0))  # 2
