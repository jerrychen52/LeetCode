def checkTwoStrings(s1: str, s2: str)->bool:
    if (len(s1) == 0 and len(s2)!=0):
        return False
    if (len(s1)!=0 and len(s2) == 0):
        return False
    p1=0
    p2=0
    num1=0
    num2=0
    L1=len(s1)
    L2=len(s2)
    while (p1<L1 and p2<L2):
        c1='?'
        c2='?'
        if (num1>0):
            num1=num1-1
            if (num1==0):
                p1+=1
        else:
            c1=s1[p1]
            p1+=1
            if (c1.isdigit()):
                num1=int(c1)
                c1='?'
        if (num2>0):
            num2=num2-1
            if (num2==0):
                p2+=1
        else:
            c2=s2[p2]
            p2+=1
            if (c2.isdigit()):
                num2=int(c2)
                c2='?'
        if (c1!='?' and c2!='?' and c1!=c2):
            return False
    if (p1!=L1 or p2!=L2):
        return False
    return True


if __name__ == '__main__':
    testInput =[["A2Le","2pL1"], ["a10","10a"],["3x2x","8"]]
    testOutput=[True,True,False]

    for i in range(len(testInput)):
        strs=testInput[i]
        outPut = checkTwoStrings(strs[0],strs[1])
        print("Input={} output={} expected={} Mathc={}".format(testInput[i],outPut,testOutput[i],outPut==testOutput[i]))
