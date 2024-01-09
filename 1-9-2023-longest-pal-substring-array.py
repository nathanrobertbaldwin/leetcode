# Given a string s of all lowercase letters, return an array where the value at each index
# is the length of the longest possible palindrome starting from that index in the string.


def longest_pal_array(s):
    res = [0] * len(s)
    idxs = range(0, len(s))

    for i in idxs:
        # worst case record palindrome length of 1
        res[i] = 1

        # for each letter in string, test if it's the center of a palindrome.
        d = 1
        while i - d in idxs and i + d in idxs and s[i - d] == s[i + d]:
            # for each delta, if still a palindrome, then
            # if the new length of the palindrome is larger than
            # the current recorded length update.
            if d * 2 + 1 > res[i - d]:
                res[i - d] = d * 2 + 1
            d += 1

        # if we encounter a pair of same letters, then worst case we record palindrome length of 2
        if i + 1 in idxs and s[i] == s[i + 1]:
            res[i] = 2
            # same idea as above, but testing with 2 letters as the center of our palindrome.
            d = 1
            while i - d in idxs and i + 1 + d in idxs and s[i - d] == s[i + 1 + d]:
                if (d * 2 + 2) > res[i]:
                    res[i - d] = d * 2 + 2
                d += 1

    return res


s = "abcabba"

print(longest_pal_array(s))
