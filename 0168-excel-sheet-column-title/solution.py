class Solution(object):
    def convertToTitle(self, columnNumber):
        
        b=''
        while(columnNumber>0):
            a=columnNumber%26
            if a==0:
                b+='Z'
            elif a==1:
                b+='A'
            elif a==2:
                b+='B'
            elif a==3:
                b+='C'
            elif a==4:
                b+='D'
            elif a==5:
                b+='E'
            elif a==6:
                b+='F'
            elif a==7:
                b+='G'
            elif a==8:
                b+='H'
            elif a==9:
                b+='I'
            elif a==10:
                b+='J'
            elif a==11:
                b+='K'
            elif a==12:
                b+='L'
            elif a==13:
               b+='M'
            elif a==14:
                b+='N'
            elif a==15:
                b+='O'
            elif a==16:
                b+='P'
            elif a==17:
                b+='Q'
            elif a==18:
                b+='R'
            elif a==19:
                b+='S'
            elif a==20:
                b+='T'
            elif a==21:
                b+='U'
            elif a==22:
                b+='V'
            elif a==23:
                b+='W'
            elif a==24:
                b+='X'
            elif a==25:
                b+='Y'
            if(columnNumber>26):
                columnNumber=(columnNumber-1)//26
            else:
                break
        return (b[::-1])
        


