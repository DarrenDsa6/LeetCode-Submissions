class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total%k in freq:
                count += freq[total%k]
            freq[total%k] = freq.get(total%k, 0)+1
        return count
        
