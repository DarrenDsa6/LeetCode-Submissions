class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue

            l = i+1
            r= len(nums)-1

            while(l<r):
                sum = nums[l] + nums[r]
                if sum == -num:
                    res.append([nums[i], nums[l], nums[r]])
                    while(l<r and nums[l+1] == nums[l]):
                        l+=1
                    while(l<r and nums[r-1] == nums[r]):
                        r-=1
                    l +=1
                    r-=1
                elif sum > -num:
                    r -= 1
                else:
                    l +=1
                
        return res
