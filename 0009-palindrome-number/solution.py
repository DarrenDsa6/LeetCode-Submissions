class Solution(object):
    def isPalindrome(self, x):
        j=[]
        i=x
        if( x<0):
            return 0
        while(i!=0):
            j.append(i%10)  
            i=i//10
        p=len(j)
        if(p==2):
            if(j[1]!=j[0]):
                return 0
        else:
            for i in range(0,p//2):
                if(j[i]!=j[-(i+1)]):
                    return 0
        return 1
