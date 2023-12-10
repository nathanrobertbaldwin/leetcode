import math


def pushDominoes(dominoes):
    res = ["." for _ in dominoes]

    lIdx = 0
    rIdx = 0

    prev = None

    while rIdx < len(dominoes):
        if dominoes[rIdx] == "R":
            if prev != "R":
                prev = "R"
                res[rIdx] = "R"
                lIdx = rIdx
                rIdx += 1
            else:
                for i in range(lIdx, rIdx + 1):
                    res[i] = "R"
                prev = "R"
                lIdx = rIdx
                rIdx += 1
        elif dominoes[rIdx] == "L":
            prev = "L"
            if dominoes[lIdx] == "R":
                repeat = (rIdx - lIdx - 1) // 2
                for i in range(lIdx + 1, lIdx + 1 + repeat):
                    res[i] = "R"
                for i in range(rIdx - repeat, rIdx + 1):
                    res[i] = "L"
            else:
                for i in range(lIdx, rIdx + 1):
                    res[i] = "L"

            lIdx = rIdx
            rIdx += 1
        else:
            rIdx += 1

    if dominoes[lIdx] == "R":
        for i in range(lIdx, rIdx):
            res[i] = "R"

    return "".join(res)


print(pushDominoes("R.R.L"))
#    "LL.RRLLLRLLL.."
