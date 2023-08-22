class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p=0
        for i in nums:
            p+=1
        for i in range(0,p):
            for j in range(i+1,p):
                if(nums[i]+nums[j]==target):
                    return(i,j)
