public class Solution {
    public string LongestPalindrome(string s) {
        string result = "";
        int resLen = 0;
        for(int i=0;i<s.Length;i++){
            // If pallindrome is odd length
            int l = i; int r = i;
            while(l>=0 && r<s.Length && s[l]==s[r]){
                if(r-l+1>resLen){//Check if the new result is longer than previously saved result the length
                    result = s.Substring(l,r-l+1);
                    resLen = r-l+1;
                }
                l-=1;
                r+=1;
            }
            // If pallindrom is even length
            l = i; r = i+1;
            while(l>=0 && r<s.Length && s[l]==s[r]){
                if(r-l+1>resLen){//Check if the new result is longer than previously saved result the length
                    result = s.Substring(l,r-l+1);
                    resLen = r-l+1;
                }
                l-=1;
                r+=1;
            }
        }
        return result;
    }
}
