class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        """
        a=[]
        j=len(s)
        if j==1:
            return 0
        if s[0]==']' or s[0]==')' or s[0]=='}':
            return 0
        for i in range(0,j):
            if(s[i]=='('or s[i]=='[' or s[i]=='{'):
                a.append(s[i])
            elif(s[i]==']' or s[i]==')' or s[i]=='}'):
                if(len(a)==0):
                    return 0
                if((s[i]==')' and a[-1]=='(') or (s[i]=='}' and a[-1]=='{') or (s[i]==']' and a[-1]=='[')):
                    a.pop()
                else:
                    return 0
        if(len(a)==0):
            return 1
