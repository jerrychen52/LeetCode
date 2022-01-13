'''
https://leetcode.com/problems/interleaving-string/
'''
def isInterleave(s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        
        if (len1+len2 != len3):
            return False
        
        keyMap = {}
        
        def checkStrings(s1: str, s2: str, s3: str, len1: int, len2: int, len3: int, pos1:int,pos2:int,pos3:int)->bool:
            key = str(pos1)+"_"+str(pos2)+"_"+str(pos3)
            if (key in keyMap.keys()):
                return keyMap.get(key)
            
            retval = False
            if (pos3==len3):
                if (pos1!=len1 or pos2!=len2):
                    retval = False
                else:
                    retval = True
            else:
                if (pos1 == len1):
                    if (s2[pos2]!=s3[pos3]):
                        retval = False
                    else:
                        retval = checkStrings(s1,s2,s3,len1,len2,len3,pos1,pos2+1,pos3+1)
                elif (pos2 == len2):
                    if (s1[pos1]!=s3[pos3]):
                        retval = False
                    else:
                        retval = checkStrings(s1,s2,s3,len1,len2,len3,pos1+1,pos2,pos3+1)
                else:
                    c1 = s1[pos1]
                    c2 = s2[pos2]
                    c3 = s3[pos3]
                    
                    path1 = False
                    path2 = False
                    if (c1==c3):
                        path1 = checkStrings(s1,s2,s3,len1,len2,len3,pos1+1,pos2,pos3+1)
                    if (c2 == c3):
                        path2 = checkStrings(s1,s2,s3,len1,len2,len3,pos1,pos2+1,pos3+1)
                    retval = path1 or path2
            
            keyMap[key] = retval
            return retval
        
        return checkStrings(s1,s2,s3,len1,len2,len3,0,0,0)

print(isInterleave("aabcc","dbbca","aadbbcbcac"))