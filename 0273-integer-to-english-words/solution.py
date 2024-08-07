class Solution(object):
    def classify(self, digit):
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if digit == 0:
            return ""
        elif digit < 20:
            return less_than_twenty[digit]
        elif digit < 100:
            return tens[digit // 10] + ("" if digit % 10 == 0 else " " + less_than_twenty[digit % 10])
        else:
            return less_than_twenty[digit // 100] + " Hundred" + ("" if digit % 100 == 0 else " " + self.classify(digit % 100))

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        billion = num // 1000000000
        million = (num % 1000000000) // 1000000
        thousand = (num % 1000000) // 1000
        remainder = num % 1000

        words = ''
        if billion > 0:
            words += self.classify(billion) + ' Billion'
        if million > 0:
            words += (' ' if words else '') + self.classify(million) + ' Million'
        if thousand > 0:
            words += (' ' if words else '') + self.classify(thousand) + ' Thousand'
        if remainder > 0:
            words += (' ' if words else '') + self.classify(remainder)
        
        return words

