public class Solution {
    public int FindPermutationDifference(string s, string t) {
        int answer = 0;
        int i = 0;
        while (i<s.Length){
            answer += Math.Abs(i - t.IndexOf(s[i]));
            i += 1;
        }
        return answer;
    }
}
