def findCows(s):
    c_count = 0
    co_count = 0
    cow_count = 0

    for i in len(s):
        if s[i] == "c":
            c_count += 1
        if s[i] == "o":
            co_count += c_count
        if s[i] == "w":
            cow_count += co_count

    return cow_count


s = "OCCOWOW"
print(findCows(s))

# scan find a c, increment c_count
# keep scanning, if we find an o, increment co count by c_count
# keep scanning, if we find a w, increment cow count by co_count
# red herrings
