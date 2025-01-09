def merge(a1, a2):
    mergedArrs = []
    i = 0
    j = 0
    while i < len(a1) or j < len(a2):
        if i == len(a1):
            mergedArrs.append(a2[j])
            j += 1
        elif j == len(a2):
            mergedArrs.append(a1[i])
            i += 1
        elif a1[i] <= a2[j]:
            mergedArrs.append(a1[i])
            i += 1
        else:
            mergedArrs.append(a2[j])
            j += 1
    return mergedArrs


def sortSuffixArr(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        return merge(sortSuffixArr(a[0:mid]), sortSuffixArr(a[mid:]))


def suffixSort(s, k):
    suffixes = []

    for i in range(len(s)):
        suffixes.append(s[i:])

    sortedSuffixes = sortSuffixArr(suffixes)

    return sortedSuffixes[k - 1]


print(suffixSort("aacb", 3))
