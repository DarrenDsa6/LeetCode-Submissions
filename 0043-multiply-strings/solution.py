class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                sum_ = product + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')
        
