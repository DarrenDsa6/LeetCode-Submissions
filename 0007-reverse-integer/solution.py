class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        negative = False
        if x<0:
            x = abs(x)
            negative = True
        while(x>0):
            a = (a*10) + (x%10)
            x = x//10
        if (-2)**31<a<(2**31)-1:
            if negative:
                return -a
            else:
                return a
        else:
            return 0

