# class Solution:
#     def decodeString(self, s: str) -> str:

#         res = ""

#         k = 0
#         k_start = 0
#         sub_s = ""
#         sub_s_start = 0
#         for i in range(len(s)):
#             if s[i] == "[":
#                 k = int(s[k_start:i])
#                 s_start = i + 1
#             if s[i] == "]":
#                 sub_s = s[s_start:i]
#                 res += sub_s * k
#                 k_start = i + 1

#         return res


# class Solution:
#     def build(self, s):

#         parens = []
#         pref = ""
#         num = ""
#         for i in range(len(s)):
#             if parens == 0:
#             if len(parens) == 0:
#                 if ord(s[i]) >= 48 and ord(s[i]) <= 57:
#                     num += s[i]
#                 if ord(s[i]) >= 97 and ord(s[i]) <= 122:
#                         pref += s[i]
#             if s[i] == "[":
#                 parens.append(i)
#             if s[i] == "]":
#                 parens.pop()
#                 if len(parens) == 0:
#                     return (int(num) * pref) + Solution.build(None, s[i + 1 :])

#         return ""

#     def decodeString(self, s: str) -> str:
#         return Solution.build(None, s)


# class Solution:
#     def build(self, s):

#         parens = []
#         pref = ""
#         rep = ""

#         res = ""
#         for i in range(len(s)):
#             if len(parens) == 0:
#                 if ord(s[i]) >= 48 and ord(s[i]) <= 57:
#                     rep += s[i]
#                 if ord(s[i]) >= 97 and ord(s[i]) <= 122:
#                     pref += s[i]
#             if s[i] == "[":
#                 parens.append(i + 1)
#             if s[i] == "]":
#                 start_idx = parens.pop()
#                 if len(parens) == 0:
#                     res += pref + int(rep) * Solution.build(None, s[start_idx:i])
#                     rep = ""

#         if len(res) == 0:
#             return pref
#         else:
#             return res

#     def decodeString(self, s: str) -> str:
#         return Solution.build(None, s)


# class Solution:
#     def build(self, s):

#         parens = []
#         pref = ""
#         rep = ""

#         res = ""
#         for i in range(len(s)):
#             if ord(s[i]) >= 48 and ord(s[i]) <= 57:
#                 rep += s[i]
#             if ord(s[i]) >= 97 and ord(s[i]) <= 122:
#                 pref += s[i]
#             if s[i] == "[":
#                 parens.append(i + 1)
#             if s[i] == "]":
#                 start_idx = parens.pop()
#                 if len(parens) == 0:
#                     start_idx - idx
#                     res += pref + (int(rep) * Solution.build(None, s[start_idx:i]))

#         return res

#     def decodeString(self, s: str) -> str:
#         return Solution.build(None, s)


# # Example 1:

# # Input: s = "3[a]2[bc]"
# # Output: "aaabcbc"

# # Example 2:

# # Input: s = "3[a2[c]]"
# # Output: "accaccacc"
# # needs to be recursive


# # Example 3:

# # Input: s = "2[abc]3[cd]ef"
# # Output: "abcabccdcdcdef"


# class Solution:
#     def decodeString(self, s: str) -> str:
#         idx = []
#         pairs = []

#         for i in range(len(s)):
#             if s[i] == "[":
#                 idx.append(i)
#             if s[i] == "]":
#                 pairs.append((idx.pop(), i))

#         for i, j in pairs:
#             mult = ""
#             pref = ""
#             k = i
#             while ord(s[k]) >= 48 and ord(s[k]) <= 57:
#                 mult += s[k]
#                 k -= 1
#             while ord(s[k]) >= 97 and ord(s[k]) <= 122:
#                 pref += s[k]
#                 k -= 1
#             if len(mult):
#                 mult = int(mult)

#             s = s[0:k] + (pref + mult * s[i + 1 : j]) + s[j + 1 :]

#         return s


# class Solution:
#     def decodeString(self, s: str) -> str:
#         pars = []
#         recurse = False
#         for i in range(len(s)):
#             if s[i] == "[":
#                 pars.append(i + 1)
#                 recurse = True
#             if s[i] == "]":
#                 start = pars.pop()
#                 if len(pars) == 0:
#                     if recurse == True:
#                         s


# class Solution:
#     def decodeString(self, s: str) -> str:
#         base = True
#         pars = []
#         mult = ""
#         for i in range(len(s)):
#             if s[i] == "[":
#                 pars.append(i)
#                 base = False
#             elif s[i] == "]":
#                 start = pars.pop() + 1
#                 end = i

#             if base == True:
#                 return s[start:end]
#             else:
#                 s = s[0:start] + Solution.decodeString(s[start:end]) + s[]

class Solution:
    def decodeString(self, s: str) -> str:
        for i in e

print(Solution.decodeString(None, "3[a]2[bc]"))
# print(Solution.decodeString(None, "3[a2[c]]"))
# print(Solution.decodeString(None, "2[abc]3[cd]ef"))
