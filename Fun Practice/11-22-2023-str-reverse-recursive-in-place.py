def reverseString(s: [str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    def reverser(left, right):
        if left >= right:
            return
        else:
            t = s[right]
            s[right] = s[left]
            s[left] = t
            reverser(left + 1, right - 1)

    reverser(left, right)


print(reverseString(["H", "e", "l", "l", "o"]))
