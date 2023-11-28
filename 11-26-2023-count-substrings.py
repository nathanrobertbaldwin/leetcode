def countBinarySubstrings(s):
    ones_needed = []
    zeroes_needed = []

    count = 0

    for i in range(0, len(s)):
        if s[i] == "0":
            ones_needed.append("1")

            if len(zeroes_needed) > 0:
                zeroes_needed.pop()
                count += 1

            if len(zeroes_needed) > 0 and s[i + 1] == "1":
                zeroes_needed = []

        if s[i] == "1":
            zeroes_needed.append("0")

            if len(ones_needed) > 0:
                ones_needed.pop()
                count += 1
            
            if len(ones_needed) > 0 and s[i + 1] == "0":
                ones_needed = []

    return count


print(countBinarySubstrings("11001111101100"))
