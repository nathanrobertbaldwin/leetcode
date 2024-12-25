# def minDistance(self, word1: str, word2: str) -> int:
#     # find max shared substring

#     dp = [[0 for _ in word2] for _ in word1]

#     for i in range(len(word1)):
#         for j in range(len(word2)):
#             # if we find same letters
#             if word1[i] == word2[j]:
#                 # if indices are in bounds
#                 if i - 1 >= 0 and j - 1 >= 0:
#                     # we update to show we have found another shared letter
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = 1

#             else:
#                 # if both i and j are in range, we want the max of current row/column,
#                 # prior row/current column, and current row/prior column
#                 if i - 1 >= 0 and j - 1 >= 0:
#                     dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
#                 elif i - 1 >= 0:
#                     dp[i][j] = max(dp[i][j], dp[i - 1][j])
#                 else:
#                     dp[i][j] = max(dp[i][j], dp[i][j - 1])

#     # absolute difference of lengths gives necessary inserts/deletes.
#     # difference of word2 length and longest shared substring gives number of swaps
#     for i in range(len(dp)):
#         print(word1[i], dp[i])

#     return abs(len(word1) - len(word2)) + (len(word2) - dp[-1][-1])


def minDistance(self, s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from s1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into s1 to match s2

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Deletion
                    dp[i][j - 1],  # Insertion
                    dp[i - 1][j - 1],
                )  # Substitution

    for i in range(len(dp)):
        print(dp[i])

    return dp[m][n]


# Example usage
s1 = "intention"
s2 = "execution"
print(minDistance(None, s1, s2))  # Output: 5


# a = "intention"
# b = "tionexecu"
# a = "xi"
# b = "yi"

# print(minDistance(None, a, b))

# swaps combine a delete and insertion
# if the words are different lengths, you must do inserts/deletes to make them same length
# difference of word2 length and longest shared substring does not give number of swaps.
# take the fewest number of ops to unite substrings?
