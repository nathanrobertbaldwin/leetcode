def myPow(x: float, n: int) -> float:
    def calc(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        flip = False if n > 0 else True
        n = -n if n < 0 else n
        odd = False if n % 2 == 0 else True
        n = n if odd == False else (n - 1)

        half = calc(x, n / 2)

        if flip is False:
            return half * half if odd is False else half * half * x
        if flip is True:
            return 1 / (half * half) if odd is False else 1 / (half * half * x)

    return calc(x, n)


print(myPow(2, -1))
