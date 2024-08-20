public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        bool[] answer = new bool[candies.Length];
        for (int i=0;i<candies.Length;i++){
            int temp = extraCandies + candies[i];
            answer[i] = temp >= candies.Max();
        }
        return answer;
    }
}
