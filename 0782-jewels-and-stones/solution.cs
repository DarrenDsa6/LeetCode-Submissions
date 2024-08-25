public class Solution {
    public int NumJewelsInStones(string jewels, string stones) {
        int count = 0;
        foreach(char c in jewels){
            count += stones.Count(d => d == c);
        }
        return count;
    }
}
