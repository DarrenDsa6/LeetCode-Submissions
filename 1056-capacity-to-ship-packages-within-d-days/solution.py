class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        while(start<=end):
            mid = (start+end)//2
            day = 1
            temp = mid
            for i in range(len(weights)):
                if(temp-weights[i]>=0):
                    temp-=weights[i]
                else:
                    temp = mid
                    temp-=weights[i]
                    day+=1
            if(day<=days):
                end = mid-1
            else:
                start=mid+1
        return start



