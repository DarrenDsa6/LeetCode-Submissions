class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = -1
        n = len(nums) - 1
        end = n
        for i in range(n):
            if nums[i] > nums[i+1]:
                start = i
                break

        for j in range(n, 0, -1):
            if nums[j] < nums[j-1]:
                end = j
                break

        if start == -1:
            return 0

        maxEle = max(nums[start: end+1])
        minEle = min(nums[start: end+1])

        while(start>0 and nums[start-1]>minEle):
            start-=1

        while(end<n and nums[end+1]<maxEle):
            end+=1
        
        return end-start+1
