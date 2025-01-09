from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + word
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                length = int(s[i])
                i += 1
                res.append(s[i : i + length])
                i += length
        return res


input = ["neet", "code", "love", "you"]
input = [""]
encode = Solution.encode(None, input)
print(encode)
print(Solution.decode(None, encode))
