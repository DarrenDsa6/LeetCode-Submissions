class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curr_max = curr_min = ans_max = ans_min = nums[0]

        for x in nums[1:]:
            curr_max = max(x, curr_max + x)
            ans_max = max(ans_max, curr_max)

            curr_min = min(x, curr_min + x)
            ans_min = min(ans_min, curr_min)

        if ans_max < 0:  # all numbers negative
            return ans_max
        return max(ans_max, total - ans_min)

