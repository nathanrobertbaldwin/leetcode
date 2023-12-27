# input: n = str input, binary representation of number
# input: k = number of times to equal max

# You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string. The maximum binary number formed after performing (possibly ) the operation is . Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string  will be equal to  for the

# time.

# Video approach to solve this question: here

# Input format

#     First line: A single integer

#  denoting the number of test cases
# For each test case:

#     First line: Two space-separated integers

# and
# Second line:

#          denoting the string

# Output format

# For each test case, print a single line containing one integer that represents the number of cyclic shift operations performed such that the value represented by string
# is equal to for the time.


def cyclic_shifts(n, k):
    max_idxs = []
    n = n[-1] + n[0 : len(n) - 1]
    max_num = n

    for shift_count in range(0, len(n)):
        n = n[1 : len(n)] + n[0]

        if n > max_num:
            max_num = n
            max_idxs = [shift_count]

        elif n == max_num:
            max_idxs.append(shift_count)

    full_loops = (k - 1) // len(max_idxs)
    full_loop_shifts = full_loops * len(n)
    count_maxs = full_loops * len(max_idxs)

    maxs_remaining = k - count_maxs
    total_shifts = full_loop_shifts + max_idxs[maxs_remaining - 1]

    return total_shifts


print(
    cyclic_shifts(
        "0101",
        2,
    )
)
