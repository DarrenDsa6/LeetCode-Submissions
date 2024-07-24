class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)

        for i in range(length):
            x = nums[i]
            a = 0
            negative = False
            if x<0:
                x = abs(x)
                negative = True
            while(x>0):
                a = (a*10) + (x%10)
                x = x//10
            nums.append(a)
        nums = set(nums)
        return len(nums)
            
            
