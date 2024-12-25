def getSMap(s):
    sMap = {}
    for i in range(0, len(s)):
        if s[i] in sMap:
            sMap[s[i]].append(i)
        else:
            sMap[s[i]] = [i]

    return sMap


def isPal(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True

def whyNotPal(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return [i, len(s) - 1 - i]

def findLongestPal(subS, mask = set()):
    
    if isPal(subS):
        return subS
    else:
        whyNotPal(subS)
        

    if isPalindrome == True:
        return


def longestPalindromeSubseq(s):
    sMap = getSMap(s)

    longestSubS = ""

    for letter in sMap:
        leftIdx = sMap[letter][0]
        rightIdx = sMap[letter][len(sMap[letter]) - 1] + 1
        letterSubS = s[leftIdx:rightIdx]
        lettersLongestSubS = findLongestPal(letterSubS)
        longestSubS = (
            longestSubS if len(longestSubS) > lettersLongestSubS else lettersLongestSubS
        )


print(isPal("babab"))
print(longestPalindromeSubseq("bbbab"))
