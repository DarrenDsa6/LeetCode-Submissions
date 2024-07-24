class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = 0
        first = num
        second = 0
        negative = False
        if num<0:
            num = abs(num)
            negative = True
        while(num>0):
            a = (a*10) + (num%10)
            num = num//10
        while a>0:
            second = (second*10) + (a%10)
            a = a//10
        if first == second:
            return True
        else:
            return False
