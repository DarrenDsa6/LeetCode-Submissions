class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        d = {s[0]:1}
        length = 1
        l = 0
        r = 1
        while(r<len(s)):
            if(d.get(s[r], 0) > 0):
                length = max(length, r - l)
                while(s[l]!=s[r]):
                    del d[s[l]]
                    l+=1
                del d[s[l]]
                l+=1
            
            d[s[r]] = 1
            r+=1
        
        return max(length, r - l)
            

        

