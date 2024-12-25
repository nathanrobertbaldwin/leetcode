import math


def encryption(s):
    sqrt = math.sqrt(len(s))
    num_rows = math.floor(sqrt)
    num_cols = math.ceil(sqrt)

    cypher = []

    l = 0
    r = num_cols
    while l < len(s):
        if r < len(s):
            cypher.append(s[l:r])
        else:
            rem = s[l:]
            rem_len = len(rem)
            pad = " " * (num_cols - rem_len)
            cypher.append(rem + pad)
        l = r
        r += num_cols

    encrypted = ""

    print(cypher)
    i = 0
    j = 0
    while j < len(cypher[0]):
        while i < len(cypher):
            if cypher[i][j] != " ":
                encrypted += cypher[i][j]
            i += 1

        encrypted += " "
        i = 0
        j += 1

    return encrypted


print(encryption("chillout"))
