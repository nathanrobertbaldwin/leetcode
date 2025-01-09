def kthGrammar(n: int, k: int):
    def strBuilder(n, k, str):
        if n == 1:
            return str
        else:
            new_str = ""
            for i in range(0, len(str)):
                if str[i] == "0":
                    new_str += "01"
                if str[i] == "1":
                    new_str += "10"
            return strBuilder(n - 1, k, new_str)

    return strBuilder(n, k, "0")


print(kthGrammar(30, 1))
