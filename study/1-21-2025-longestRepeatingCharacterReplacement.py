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

# Constraints:

#     1 <= s.length <= 1000
#     0 <= k <= s.length


# Solution: For each character in the string, use a freq counter to
# keep track of it's count. maxf is used to consistently update
# which character is the most frequent. We only care about
# the most frequent character in a range. The other chars
# cause us to have to consider replacements, k. The key
# here is that (r - l + 1) - maxf, i.e. the number of chars in a range
# minus the most frequent char in that range, must be less than k.
# If not, we need to reduce the size of the (r - l) + 1 range.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # Updates maxf every loop. i.e. We check if the current
            # char is most frequent.
            maxf = max(maxf, count[s[r]])

            # This is how we deal with replacements.
            # If the number of characters between R and L, minus maxf,
            # is greater than the number of replacements we can make,
            # we need to bring in the left pointer.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s) # O(n) to add chars to the set

        for c in charSet: #O(m), where m is num of unique chars
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res


# print(Solution.characterReplacement(None, "XYYX", 2))
print(Solution.characterReplacement(None, "AAABABB", 1))
