class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for i in strs[1:]:
            while i[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ''
        return prefix
            
        
