class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = float('inf')
        start = 1
        end = max(bloomDay)
        if len(bloomDay)<m*k:
            return -1
        while(start<=end):
            curr = 0
            mid = (start+end)//2
            cont = 0
            for i in bloomDay:
                if i<=mid:
                    cont+=1
                else:
                    cont = 0
                if cont>=k:
                    cont = 0
                    curr+=1
            if(curr>=m):
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans
