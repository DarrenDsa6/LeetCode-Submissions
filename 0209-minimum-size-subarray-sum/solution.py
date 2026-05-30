class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        total = nums[j]
        ans = 0
        count = 1
        while(j<len(nums) and i<=j and i<len(nums)):
            if(total < target):
                j+=1
                if(j<len(nums)):
                    total += nums[j]
                count += 1
            elif(total >= target):
                if(ans == 0):
                    ans = count
                else:
                    ans = min(count, ans)
                    if(i==j):
                        j+=1
                        if(j<len(nums)):
                            total += nums[j]
                            count+=1
                    total -= nums[i]
                    i+=1
                    count -= 1
        return ans



        
