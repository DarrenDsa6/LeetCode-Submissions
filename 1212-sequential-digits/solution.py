class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        st = "123456789"
        ans = []
        for digits in range(len(str(low)), len(str(high)) + 1):
            for i in range(len(st) - digits + 1):
                num = int(st[i:i+digits])
                if low <= num <= high:
                    ans.append(num)
        return ans

