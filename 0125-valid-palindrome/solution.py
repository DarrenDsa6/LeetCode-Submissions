class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        b   = ''
        for i in range(len(s)-1,-1,-1):
            b += s[i]
        if s==b:
            return True
        return False
