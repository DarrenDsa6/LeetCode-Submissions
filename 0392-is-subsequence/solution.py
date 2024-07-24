class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        i = 0
        while a<len(t):
            if i<len(s) and s[i] == t[a]:
                i += 1
            a+=1
        if i == len(s):
            return True
        return False
