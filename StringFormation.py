
from typing import Counter, List
import sys

class StringFormation:
    def stringForm(self,words: List[str], targ: str):
        M = 10**9 +7
        ln = len(words[0])
        ctr = Counter()
        for w in words:
            for i,ch in enumerate(w):
                ctr[i,ch] += 1
        dp = [0]*(len(targ)+1)
        dp[0] = 1
        for i in range(1,ln+1):
            dp2 = [0]*(len(targ)+1)
            dp2[0] = 1
            for j in range(1,len(targ)+1):
                dp2[j] = dp[j]   # jth position in targ could be filled before ith index of words[][i]
                dp2[j] += dp[j-1]*ctr[i-1,targ[j-1]]  # number of formed target strings of length j-1 * count of jth letter at pos i in words
            dp = dp2
        return dp[len(targ)] % M

if __name__ == '__main__':
    sf = StringFormation()

    testInput1 = [["abc","aec","def"],["valyq","lyglb","vldoh"], ["xzu","dfw","eor","mat","jyc"]]
    testInput2=["ac","val","cf"]
    testResult=[4,4,0]

    n =len(testInput1)
    for i in range(n):
        words=testInput1[i]
        target=testInput2[i]
        result=sf.stringForm(words,target)
        print("Input={}\t\texpected={}\t\tresult={}\t\tmatch={}".format(testInput1[i],testResult[i],result,testResult[i] == result))

