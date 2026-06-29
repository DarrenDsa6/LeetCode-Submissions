class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in nums[1:]:
            temp = curr_max
            curr_max = max(i, i * curr_max, i * curr_min)
            curr_min = min(i, i * temp, i * curr_min)
            ans = max(ans, curr_max)

        return ans
