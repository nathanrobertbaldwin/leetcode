from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ["()"]
        res = set()

        while len(stack) > 0:
            s = stack.pop()
            if len(s) == n * 2:
                res.add(s)
            else:
                for i in range(len(s) - 1):
                    if s[i] == "(" and s[i + 1] == ")":
                        stack.append(s[0:i] + "(())" + s[i + 2 :])
                        stack.append(s[0:i] + "()()" + s[i + 2 :])
                        
        return list(res)


n = 4
print(Solution.generateParenthesis(None, n))
