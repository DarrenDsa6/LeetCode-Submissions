class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length_1 = len(num1) - 1
        length_2 = len(num2) - 1
        result = ''
        carry = 0
        while length_1 >= 0 or length_2 >= 0 or carry:
            digit1 = ord(num1[length_1]) - ord('0') if length_1 >= 0 else 0
            digit2 = ord(num2[length_2]) - ord('0') if length_2 >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            result = str(total % 10) + result
            length_1 -= 1
            length_2 -= 1
        return result
