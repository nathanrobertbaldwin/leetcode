class Solution:
    def isValid(self, s: str) -> bool:
        closingPars = []

        for c in s:
            if c == "[":
                closingPars.append("]")
            elif c == "(":
                closingPars.append(")")
            elif c == "{":
                closingPars.append("}")
            else:
                if len(closingPars) == 0:
                    return False

                closingPar = closingPars.pop()

                if closingPar != c:
                    return False

        return True


s = "[(])"
print(Solution.isValid(None, s))
