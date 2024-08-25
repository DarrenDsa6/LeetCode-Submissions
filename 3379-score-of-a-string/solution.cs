public class Solution {
    public int ScoreOfString(string s) {
        int j = 1;
        int answer = 0;
        while(j<s.Length){
            answer += Math.Abs((int)s[j-1] - (int)s[j]);
            j+=1;
        }
        return answer;
    }
}
