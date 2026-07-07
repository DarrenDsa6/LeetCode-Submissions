class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        ans = abs(nums[0])

        for i in range(1,len(nums)):
            curr_min = min(nums[i], curr_min+nums[i])
            curr_max = max(nums[i], curr_max+nums[i])
            ans = max(ans, abs(curr_max), abs(curr_min))
        
        return ans




        
