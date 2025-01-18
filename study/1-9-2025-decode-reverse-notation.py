from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for c in tokens:
            if ord(c[-1]) >= 48 and ord(c[-1]) <= 59:
                s.append(int(c))
            else:
                num1 = s.pop()
                num2 = s.pop()
                if c == "+":
                    s.append(num1 + num2)
                elif c == "-":
                    s.append(num1 - num2)
                elif c == "*":
                    s.append(num1 * num2)
                elif c == "/":
                    s.append(num1 // num2)

        return s[0]


# tokens = ["1", "2", "+", "3", "*", "4", "-"]
# tokens = ["1", "2", "+", "3", "*", "4", "-"]
# tokens = ["2", "-3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["3", "-4", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution.evalRPN(None, tokens))
