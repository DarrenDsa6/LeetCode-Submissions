class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = -1
        right = 0
        left = 0
        freq = {}
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            if len(freq) <= 2:
                ans = max(ans, right - left + 1)
        return ans

                        
