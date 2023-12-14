def validParens(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(")")
        else:
            if len(stack) == 0:
                return False

            par = stack.pop(len(stack) - 1)

            if par != ")":
                return False

    if len(stack) > 0:
        return False

    return True


def generateParenthesis(n):
    def parensGenerator(n, str, valid=[]):
        if len(str) == n * 2:
            if validParens(str) == True:
                valid.append(str)

        else:
            parensGenerator(n, str + "(", valid)
            parensGenerator(n, str + ")", valid)

        return valid

    parenCombos = parensGenerator(n, "")
    return parenCombos


print(generateParenthesis(3))
