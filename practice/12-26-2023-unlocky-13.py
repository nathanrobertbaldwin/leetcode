import math

# Total number of strings that we can produce with n digits using 0 - 9, no restrictions.


def total_combos(n):
    return 10**n


# From total_combos, we subtract the total number of strings with the substring '13' in it.
# This takes two steps:

# Step one: For given n, how many substrings contain "13"?

# For n = 4, we create the following groups of strings with a substring of "13"

# xx13
# x13x
# 13xx

## Total groups = 3

## For n = 5, we can generate the following groups of strings with a substring of "13"

## xxx13
## xx13x
## x13xx
## 13xxx

# Groups = 4

# i.e. We can generate (n - 1) groups of strings with a substring of "13"

# Since we have have the digits 0 - 9 at each "x" in these substrings, each group will have 10 ** (n - 2) substrings.
# Hence:


def combos_with_13(n):
    return 10 ** (n - 2) * (n - 1)


def _testing_combos_of_duplicates(combo):
    nums = "0123456789"

    combos = []

    def maker(combo):
        if "x" in combo:
            for i in range(0, len(combo)):
                if combo[i] == "x":
                    for j in range(0, len(nums)):
                        combo = combo[:i] + nums[j] + combo[i + 1 :]
                        maker(combo)
        else:
            combos.append(combo)

    maker(combo)
    return combos


# However, this pattern of identifying groups of substrings containing "13" creates duplicates.
# For example, for n = 7 we have duplicates where:

# The number of groups of duplicates to add back in is n choose k, or: C(n, k) = n! / (k!(n - k)!)


def add_back_duplicates(n):
    return (10 ** (n - 4)) * (
        math.factorial(n - 2)
        // (math.factorial(n - 4) * math.factorial((n - 2) - (n - 4)))
    )


def total_strs_without_13(n):
    return (total_combos(n) - combos_with_13(n) + add_back_duplicates(n)) % 1000000009


def brute_force_13s(n):
    thirteens = set()
    others = set()
    digits = "0123456789"

    def maker(n, curr_string=""):
        if len(curr_string) == n:
            if "13" in curr_string:
                thirteens.add(curr_string)
            else:
                others.add(curr_string)
        elif len(curr_string) < n:
            for i in range(0, 10):
                maker(n, curr_string + digits[i])

    maker(n)
    return ("13s", len(thirteens), "valid", len(others))


n = 6

correct = brute_force_13s(n)

t = total_combos(n)
m = combos_with_13(n)
p = add_back_duplicates(n)

my_total = t - m + p

print("Correct Answer:", correct)
print("---------------------")
print("Total Combos:", t)
print("- 13 Combos", m)
print("+ Dups:", p)
print("_____________________")
print("My total:", my_total)
print("Diff", correct - my_total)
print("dups should be", correct - (my_total - p))

# for 6
potential_combos = {"xx1313", "13xx13", "1313xx", "x13x13", "x1313x", "13x13x"}

all_dup_combos_arr = []
all_dup_combos_set = set()
for combo in potential_combos:
    res = _testing_combos_of_duplicates(combo)
    all_dup_combos_arr += res
    all_dup_combos_set.update(res)

# for 7
# potential_combos = {
#     "xx13x13",
#     "13x13xx",
#     "x13x13x",
#     "13xxx13",
#     "xx1313x",
#     "1313xxx",
#     "13xx13x",
#     "x1313xx",
#     "xxx1313",
#     "x13xx13",
# }

print(len(all_dup_combos_arr))
print(len(all_dup_combos_set))
