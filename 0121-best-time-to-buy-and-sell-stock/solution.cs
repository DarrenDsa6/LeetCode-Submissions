public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length == 0) return 0;  // Edge case: empty array
        
        int profit = 0;
        int min = prices[0];  // Initialize min with the first price
        
        // Start the loop from the second element (index 1)
        for (int i = 1; i < prices.Length; i++) {
            if (prices[i] > min) {
                profit = Math.Max(profit, prices[i] - min);
            } else {
                min = Math.Min(min, prices[i]);  // Update the minimum price if necessary
            }
        }
        
        return profit;  // Return the maximum profit
    }
}

