class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = dict()
        shortest_i = 0
        shortest_j = len(s)
        updated = False

        for c in t:
            needed[c] = 1 + needed.get(c, 0)

        for i in range(len(s)):
            if s[i] in needed:
                have = dict()
                for j in range(i, len(s)):
                    if s[j] in needed:
                        if s[j] in have:
                            if have[s[j]] < needed[s[j]]:
                                have[s[j]] = 1 + have.get(s[j])
                        else:
                            have[s[j]] = 1
                    if have == needed:
                        updated = True
                        if j - i + 1 < shortest_j - shortest_i + 1:
                            shortest_i = i
                            shortest_j = j

        if updated == False:
            return ""
        else:
            return s[shortest_i : shortest_j + 1]


print(Solution.minWindow(None, s="ADOBECODEBANC", t="ABC"))
# print(Solution.minWindow(None, s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))
