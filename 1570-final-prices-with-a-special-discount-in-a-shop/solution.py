class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices
        for i in range(len(prices)):
            j = i+1
            while j<len(prices) and prices[j]>prices[i]:
                j+=1
            if j < len(prices) and prices[j]<=prices[i]:
                prices[i] = (prices[i]-prices[j])
        return prices
