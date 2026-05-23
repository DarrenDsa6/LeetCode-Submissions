class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0]*(len(height))
        rmax = [0]*(len(height))
        ans = 0
        lmax[0] = height[0]
        rmax[len(height)-1] = height[len(height)-1]
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])

        for i in range(len(height)):
            ans+= min(lmax[i], rmax[i])- height[i]
        return ans
