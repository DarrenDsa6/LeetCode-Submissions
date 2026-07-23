class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start =1
        end = max(candies)
        ans = 0
        while(start<=end):
            mid = (start+end)//2
            curr = 0
            for i in range(len(candies)):
                curr += candies[i]//mid
            if curr>=k:
                start = mid+1
                ans = max(ans, mid)
            else:
                end = mid-1
        return ans
            
        
