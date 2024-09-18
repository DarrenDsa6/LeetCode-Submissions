public class Solution {
    public string MinWindow(string s, string t) {
        Dictionary<char, int> map = new Dictionary<char, int>();

        foreach(char c in t){
            if(map.ContainsKey(c)){
                map[c]++;
            }
            else{
                map.Add(c,1);
            }
        }
        int start=0, min=int.MaxValue ,match=0, ans_start=0;

        for(int stop = 0; stop<s.Length; stop++){
            if(map.ContainsKey(s[stop])){
                map[s[stop]]--;
                if(map[s[stop]]==0) match++;
            }

            while(match==map.Count){
                if( min > stop - start + 1){
                    min = stop - start+1;
                    ans_start = start;
                }

                char del = s[start++];
                if (map.ContainsKey(del)){
                    map[del]++;
                    if (map[del] == 1) match--;
                }
            }
        }
        return min == int.MaxValue ? "" : s.Substring(ans_start, min);
    }
}

