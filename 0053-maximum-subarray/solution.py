class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            if(nums[i]>total+nums[i]):
                total = nums[i]
            else:
                total += nums[i]
            ans = max(ans, total)
        return ans

        
