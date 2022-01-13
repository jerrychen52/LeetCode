def isScramble(s1: str, s2: str) -> bool:
    if (len(s1)!=len(s2)):
        return False
    dictSub = {}
    def isScrambleSub(s1:str,s2:str)->bool:
            print("s1={} s2={}".format(s1,s2))
            if (len(s1)==1):
                return s1 == s2
            if (len(s1)!=len(s2)):
                return False  
            if (s1==s2):
                return True;
                
            key = s1+s2
            if (key in dictSub.keys()):
                return dictSub[key]
            charCnt  = [0]*26
            for c in s1:
                charCnt[ord(c)-ord('a')]+=1
            for c in s2:
                charCnt[ord(c)-ord('a')]-=1
            for i in range(0,26):
                if charCnt[i] !=0:
                    dictSub[key] = False
                    return False
            retval = False
            for i in range(1,len(s1),1):
                if  ((isScrambleSub(s1[0:i],s2[0:i]) and isScrambleSub(s1[i:len(s1)],s2[i:len(s1)])) or (isScrambleSub(s1[0:i],s2[len(s1)-i: len(s1)]) and isScrambleSub(s1[i:len(s1)],s2[0:len(s1)-i]))):
                    retval = True
                    break;
            
            dictSub[key] = retval
            return retval
    return isScrambleSub(s1,s2)

print(isScramble("gr", "rg"))