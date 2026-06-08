class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = -1
        zeroCount = 0
        for right in range(0,len(nums)):
            if(nums[right]==0):
                zeroCount += 1
            while(zeroCount>k):
                if(nums[left] == 0):
                    zeroCount -= 1
                left+=1
            ans = max(right-left+1, ans)
        return ans
