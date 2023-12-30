def mult(num1, num2):
    return num1 * num2


def add(num1, num2):
    return num1 + num2


def find_left_num(e, idx):
    start = idx + 1

    while idx >= 0 and e[idx] != "+" and e[idx] != "*":
        idx -= 1

    return [int(e[idx + 1 : start]), idx + 1]


def find_right_num(e, idx):
    start = idx

    while idx < len(e) and e[idx] != "+" and e[idx] != "*":
        idx += 1

    return [int(e[start:idx]), idx]


def eval_string(e):
    for left in range(len(e)):
        if e[left] == "(":
            count = 1
            right = left + 1
            while count > 0:
                right += 1
                if e[right] == "(":
                    count += 1
                if e[right] == ")":
                    count -= 1
            update = str(eval_string(e[left + 1 : right]))
            e = e[0:left] + update + e[right + 1 :]
            return eval_string(e)

    for i in range(len(e) - 1):
        if e[i] == "*":
            [num1, left] = find_left_num(e, i - 1)
            [num2, right] = find_right_num(e, i + 1)
            update = str(mult(num1, num2))
            e = e[0:left] + update + e[right:]
            return eval_string(e)

    for i in range(len(e) - 1):
        if e[i] == "+":
            [num1, left] = find_left_num(e, i - 1)
            [num2, right] = find_right_num(e, i + 1)
            update = str(add(num1, num2))
            e = e[0:left] + update + e[right:]
            return eval_string(e)

    return e


expression = "(((1 + 1)))"
print("Your output  ", eval_string(expression))
print("Expected     ", eval(expression))
