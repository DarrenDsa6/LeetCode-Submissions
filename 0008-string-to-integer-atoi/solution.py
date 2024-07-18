class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        negative = False
        ans = 0
        if s[0]=='-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            negative = False
            s = s[1:]
        i = 0
        while i<len(s) and s[i].isdigit():
            ans *= 10
            ans = (ord(s[i]) - ord('0')) + ans
            i+=1
        if negative:
            ans = -ans
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
        return ans
            
