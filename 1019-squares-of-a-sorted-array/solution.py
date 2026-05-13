class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [0] * len(nums)
        index = r
        for i in range(0, len(nums)):
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            if(left>right):
                ans[index] = left
                l+=1
            if(right>=left):
                ans[index] = right
                r-=1
            index -=1
        return ans


        
