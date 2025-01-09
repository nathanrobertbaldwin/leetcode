def convertToBase7(n):
    base7 = ""

    negative = False
    if n < 0:
        negative = True
        n = -n

    while n > 0:
        remainder = n % 7
        base7 = str(remainder) + base7
        n = n // 7

    return base7 if negative == False else "-" + base7


print(convertToBase7(7))
