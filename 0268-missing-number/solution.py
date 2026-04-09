class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        ans = (s + 1) * (s) // 2
        total = 0
        for i in nums:
            total += i
        return ans - total
