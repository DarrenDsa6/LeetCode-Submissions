class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_capacity = 0
        while left < right:
            min_height = min(height[left], height[right])
            current_capacity = min_height * (right - left)
            max_capacity = max(max_capacity, current_capacity)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_capacity

