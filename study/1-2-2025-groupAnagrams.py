from typing import List

# While this solution does delete entries from the list of strings when
# the algorithm finds they belong to the same group, it will retest other strings.
# class Solution:
#     def char_counter(s):
#         counter = dict()
#         for c in s:
#             if c in counter:
#                 counter[c] += 1
#             else:
#                 counter[c] = 1
#         return counter

#     def groupAnagrams(strs: List[str]) -> List[List[str]]:

#         res = []

#         while len(list(strs)) > 0:
#             s = strs.pop()
#             s_char_count = Solution.char_counter(s)

#             group = [s]
#             for other_s in list(strs):
#                 other_s_char_count = Solution.char_counter(other_s)

#                 if s_char_count == other_s_char_count:
#                     group.append(other_s)
#                     strs.remove(other_s)

#             res.append(group)

#         return res


# This solution creates a counter for each string only once. We store
# the sorted, tupled counter as a key in a dictionary, where the values are
# all the strings with the same sorted, tupled counter.
class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        encodings = dict()
        for s in strs:
            encode = dict()
            for char in s:
                if char in encode:
                    encode[char] += 1
                else:
                    encode[char] = 1
            encode = tuple(encode.items())
            if encode in encodings:
                encodings[encode].append(s)
            else:
                encodings[encode] = [s]
        return list(encodings.values())


strs = ["", ""]
strs = ["ddddddddddg", "dgggggggggg"]
print(Solution.groupAnagrams(strs))
