class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        if digits[-1] == 10:
            i = len(digits)-1
            while i>0 and digits[i] == 10:
                digits[i] = 0
                digits[i-1] = digits[i-1]+1
                i -= 1
            if digits[0] == 10:
                digits[0] = 0
                digits.insert(0, 1)
        return digits
