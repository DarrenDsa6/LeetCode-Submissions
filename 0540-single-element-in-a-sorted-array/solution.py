class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        Left = 0
        n = len(nums)
        Right = n -1
        while(Left<Right):
            Mid = (Left+Right)//2
            if Mid % 2 == 1:
                Mid -= 1
            if nums[Mid] == nums[Mid + 1]:
                Left = Mid + 2
            else:
                Right = Mid
        return nums[Left]

