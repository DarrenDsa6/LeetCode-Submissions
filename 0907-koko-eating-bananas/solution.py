from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            # Calculate hours needed at speed = mid
            curr = sum(math.ceil(pile / mid) for pile in piles)
            
            if curr <= h:
                ans = mid
                high = mid - 1  # try slower speed
            else:
                low = mid + 1   # need faster speed
        return ans

