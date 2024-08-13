public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int max = 0;
        for (int i=0; i<accounts.Length; i++){
            int sum1 = 0;
            foreach(int j in accounts[i]){
                sum1+=j;
            }
            max = (max>sum1)? max : sum1;
        }
        return max;
    }
}
