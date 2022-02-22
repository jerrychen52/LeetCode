class PerfectSquares:
    def numSquares(self, n: int) -> int:             
        tempDict = {}
        tempDict[0]=0
        def numSquareRec(n:int)->int:
            if (n in tempDict.keys()):
                return tempDict[n]
            i=1
            ans = n
            while (i*i<=n):
                ans = min(ans,numSquareRec(n-i*i)+1)
                i+=1
            tempDict[n]=ans
            return ans

        def numSquaresDP(n:int)->int:
            dp = [n]*(n+1)
            dp[0] = 0
            for i in range (1,n+1,1):
                j=1
                while (j*j<=i):
                    dp[i] = min(dp[i], dp[i-j*j]+1)
                    j+=1
            return dp[n]
        
        return numSquareRec(n)

if __name__ == '__main__':
    perSq = PerfectSquares()
    testInput= [12,13]
    testOutput = [3,2]
    n = len(testInput)
    for i in range(n):
        result= perSq.numSquares(testInput[i])
        print("n={} Expect Result={} Calculate Result={} Match={}".format(testInput[i],testOutput[i],result, testOutput[i]==result))