class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = []
        total = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                digits.append(digit)
                total += digit
            n //= 10
        digits.reverse()
        ans = 0
        for d in digits:
            ans = ans * 10 + d
        return ans * total

