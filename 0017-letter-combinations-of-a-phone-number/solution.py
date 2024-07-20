class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = ['']
        for digit in digits:
            if digit not in digit_to_char:
                continue
            chars = digit_to_char[digit]
            new_result = []
            for combination in result:
                for char in chars:
                    new_result.append(combination + char)
            result = new_result
        return result

