public class Solution {
    public string RestoreString(string s, int[] indices) {
        StringBuilder answer = new StringBuilder(s);
        int j = 0;
        foreach(int i in indices){
            answer[i] = s[j++];
        }
        return answer.ToString();
    }
}
