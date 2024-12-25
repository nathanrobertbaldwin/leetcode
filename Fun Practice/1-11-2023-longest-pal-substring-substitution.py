# Finds the length of the longest palindrome creatable from each index
# of a string while allowing for a single substitution.


# def longest_pal_by_substitution(s):
#     res = [0] * len(s)

#     for i in range(0, len(s)):
#         res[i] = 2
#         d = 1
#         sub_count = 0

#         while i - d >= 0 and i + d < len(s) and sub_count < 2:
#             if s[i - d] != s[i + d]:
#                 sub_count += 1
#             elif d * 2 + 1 > res[i - d]:
#                 res[i - d] = d * 2 + 1

#             d += 1

#         if i + 1 < len(s) and s[i] == s[i + 1]:
#             res[i] = 3
#             sub_count = 0
#             d = 1

#             while i - d >= 0 and i + 1 + d < len(s) and sub_count < 2:
#                 if s[i - d] != s[i + 1 + d]:
#                     sub_count += 1

#                 elif (d * 2 + 2) > res[i]:
#                     res[i - d] = d * 2 + 2

#                 d += 1

#     return sum(res)


# For testing: Returns a list of the longest palindromic strings creatable from each index of a string
# while allowing for a single substitution.


def longest_pal_by_substitution_answers(s):
    res = [0] * len(s)
    res[-1] = s[-1]

    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            res[i] = s[i] * min(2, len(s) - i)

            d = 1
            char = ""
            idx = None

            while i - d >= 0 and i + d < len(s):
                if s[i - d] == s[i + d]:
                    res[i - d] = s[i - d : i + d + 1]
                else:
                    if len(char) == 0:
                        char = s[i - d]
                        idx = i + d
                    else:
                        break
                d += 1

            if len(char) == 1:
                d -= 1
                subbed = s[i - d : idx] + char + s[idx + 1 : i + d + 1]
                if len(subbed) > len(res[i - d]):
                    res[i - d] = s[i - d : idx] + char + s[idx + 1 : i + d + 1]

        else:
            res[i] = s[i] * min(3, len(s) - i)
            d = 1
            char = ""
            idx = None

            while i - d >= 0 and i + d < len(s):
                if i + d + 1 < len(s):
                    if s[i - d] == s[i + d + 1]:
                        res[i - d] = s[i - d : i + d + 2]
                else:
                    if len(char) == 0:
                        char = s[i - d]
                        idx = i + d
                    else:
                        break

                d += 1

            if len(char) == 1:
                d -= 1
                subbed = s[i - d : idx] + char + s[idx + 1 : i + d + 2]
                if len(subbed) > len(res[i - d]):
                    res[i - d] = s[i - d : idx] + char + s[idx + 1 : i + d + 2]

    return res


one = "a"
# no subs
# max diff letters 1

two = "aa"
# no subs, max 1
two_1 = "ab"
# 1 sub
# max diff letters 1

three = "aaa"
# no subs, max 3
three_1 = "baa"
# one sub, max three
three_2 = "abc"
# one sub
# max diff letters = 3


four = "aaaa"
# no subs, max 4
four_1 = "baba"
four_2 = "abax"

# max we canmake is three

print(longest_pal_by_substitution_answers(a))
