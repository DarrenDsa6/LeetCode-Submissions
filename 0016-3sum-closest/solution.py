class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        least = float('inf')
        for i in range(0, length-2):
            j = i + 1
            k = length - 1
            while j<k:
                sum1 = nums[i]+nums[j]+nums[k]
                if abs(least - target) > abs(sum1 - target):
                    least = sum1
                if sum1 > target:
                    k -= 1
                elif sum1 < target:
                    j += 1
                else:
                    return sum1
        return least


