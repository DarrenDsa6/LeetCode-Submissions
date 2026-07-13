class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                # Peak is to the right
                start = mid + 1
            else:
                # Peak is at mid or to the left
                end = mid
        return start
