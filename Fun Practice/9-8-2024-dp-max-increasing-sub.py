# import random


# def find_max_increased_subsequence(a):

#     dp = [1 for _ in range(len(a))]

#     for i in range(len(a)):
#         for j in range(0, i):
#             if a[j] <= a[i]:
#                 if dp[j] + 1 > dp[i]:
#                     dp[i] = dp[j] + 1

#     print(a)
#     print(dp)
#     return max(dp)


# for test in range(5):

#     a_length = random.randint(1, 10)
#     a = []

#     for i in range(a_length):
#         a.append(random.randint(0, 100))

#     print("RESULTS")
#     print(find_max_increased_subsequence(a))
#     print("----------------------------------")


def find_bottom_touchy_path(a):

    dp = [[0 for _ in a[0]] for _ in a]
    dp[0][0] = a[0][0]

    dp2 = [[0 for _ in a[0]] for _ in a]
    dp2[0][-1] = a[0][-1]

    # initial values for dp
    col = 0
    for row in range(1, len(a)):
        dp[row][col] = a[row][col] + dp[row - 1][col]

    row = 0
    for col in range(1, len(a[0])):
        dp[row][col] = a[row][col] + dp[row][col - 1]

    for row in range(1, len(a)):
        for col in range(1, len(a)):
            dp[row][col] = a[row][col] + max(
                [dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]]
            )

    # initial values for dp2
    col = -1
    for row in range(1, len(a)):
        dp2[row][col] = a[row][col] + dp2[row - 1][col]

    row = 0

    for col in range(len(a[0]) - 2, -1, -1):
        dp2[row][col] = a[row][col] + dp2[row][col + 1]

    for row in range(1, len(a)):
        for col in range(len(a[0]) - 2, -1, -1):
            dp2[row][col] = a[row][col] + max(
                [dp2[row][col + 1], dp2[row - 1][col], dp2[row - 1][col + 1]]
            )

    ans = -9999999999999999999999999
    for shared_column in range(len(a[0])):
        right_side_choices = -9999999999999999999999999
        accumulate_of_this_column = 0

        for row_where_left_side_joins in range(len(a) - 1, -1, -1):

            accumulate_of_this_column += a[row_where_left_side_joins][shared_column]

            # index out of boundsf
            if shared_column + 1 < len(a[0]):  # if right side exists
                right_side_choices = max(
                    right_side_choices,
                    dp2[row_where_left_side_joins][shared_column + 1],
                )
            else:
                pass  # do nothing who cares LOL

            if shared_column - 1 >= 0:
                ans = max(
                    ans,
                    accumulate_of_this_column
                    + dp[row_where_left_side_joins][shared_column - 1]
                    + right_side_choices,
                )
            else:  # index out of bounds, left side doesnt exist
                ans = max(ans, accumulate_of_this_column + right_side_choices)

    return ans


a = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
]

print(find_bottom_touchy_path(a))


# print(already_ordered([1, 3], [2, 4]))


# def longest_substring_nlogn(a):

#     if len(a) <= 1:
#         return a

#     mid = len(a) // 2

#     return max(
#         already_ordered(
#             longest_substring_nlogn(a[:mid], longest_substring_nlogn(a[mid:]))
#         )
#     )

# what if I compare left vs right. If left has a larger subsequence, I check if I can append anything from right.
# if right has a larger subsequence,


# def pick_subsequence(a1, a2):

#     i = 0
#     j = 0

#     sorted = []

#     while i < len(a1):
#         if a1[i] <= a2[j]:
#             if len(sorted) == 0:
#                 sorted.append(a1[i])
#             elif a1[i] >= sorted[-1]:
#                 sorted.append(a1[i])

#         i += 1

#     while j < len(a2):
#         if len(sorted) == 0:
#             sorted.append(a2[j])
#         elif a2[j] >= sorted[-1]:
#             sorted.append(a2[j])

#         j += 1

#     return sorted


# def longest_subsequence_nLogn(a):

#     def divider(a):

#         if len(a) < 2:
#             return a

#         mid = len(a) // 2

#         return pick_subsequence(divider(a[:mid]), divider(a[mid:]))

#     sorted = divider(a)
#     return sorted


# print(longest_subsequence_nLogn([5, 6, 10, 7, 2, 3, 8, 4]))
