def climbing_stairs(n):
    def climber(n, calculated={}):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            if n in calculated:
                return calculated[n]
            else:
                calculated[n] = climber(n - 2, calculated) + climber(n - 1, calculated)
                return calculated[n]

    return climber(n)


print(climbing_stairs(10))
