class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        arr = [0,0,0]
        for j in range(len(s)):
            arr[ord(s[j]) - ord('a')]+=1
            while min(arr)>0:
                count+= len(s)-j
                arr[ord(s[i]) - ord('a')]-=1
                i+=1
        return count
