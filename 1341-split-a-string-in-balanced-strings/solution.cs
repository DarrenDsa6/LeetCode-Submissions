public class Solution {
    public int BalancedStringSplit(string s) {
        int count = 0;
        int answer = 0;
        foreach(char c in s){
            if(c=='R'){
                count += 1;
            }
            if(c=='L'){
                count -= 1;
            }
            if(count==0){
                answer+=1;
            }
        }
        return answer;
    }
}
