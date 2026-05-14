class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while(l<r):
                sum = nums[i] + nums[l]+ nums[r]
                if(abs(target - ans) >= abs(target - sum)):
                    ans = sum
                if(sum>target):
                    r-=1
                else:
                    l+=1
        return ans
                
                    
