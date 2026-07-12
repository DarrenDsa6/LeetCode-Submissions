class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = {0:-1}
        res = 0
        total = 0
        for i in range(0,len(nums)):
            if nums[i]==0:
                total-=1
            else:
                total+=1
            if total in freq:
                res = max(res, i-freq[total])
            else:
                freq[total] = i
        return res


        
