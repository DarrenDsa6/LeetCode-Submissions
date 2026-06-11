class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(p) > len(s)):
            return []
        
        sCount = [0]*26
        pCount = [0]*26
        ans=[]
        for i in range(len(p)):
            sCount[ord(s[i])-ord('a')]+=1
            pCount[ord(p[i]) - ord('a')]+=1
        
        matches = 0
        for i in range(26):
            if(sCount[i] == pCount[i]):
                matches+=1
        
        left = 0
        for right in range(len(p), len(s)):
            if(matches == 26):
                ans.append(left)
            
            index = ord(s[left]) - ord('a')
            if sCount[index] == pCount[index]:
                matches -= 1
            sCount[index] -= 1
            if sCount[index] == pCount[index]:
                matches += 1
            left += 1

            index = ord(s[right]) - ord('a')
            sCount[index]+=1
            if(sCount[index]==pCount[index]):
                matches+=1
            elif(sCount[index]-1==pCount[index]):
                matches-=1
        
        if(matches == 26):
            ans.append(left)
        
        return ans

        
