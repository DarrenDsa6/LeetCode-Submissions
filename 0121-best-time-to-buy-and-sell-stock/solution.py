class Solution(object):
    def maxProfit(self,prices):
        
        min=prices[0]
        profit=0
        for i in prices:
            if(i<min):
                min=i
            else:
                profit=max(profit,i-min)
        return profit
