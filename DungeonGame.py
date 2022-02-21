# https://leetcode.com/problems/dungeon-game/
from typing import List
import sys
class DungeonGame:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:
            return 1 if dungeon[0][0] > 0 else abs(dungeon[0][0]) +1
        
        dp = []
        for i in range(m+1):
            dp.append([ -sys.maxsize-1]*(n+1))
        
        dp[m-1][n-1] = dungeon[m-1][n-1]
        if (dp[m-1][n-1]>0):
            dp[m-1][n-1] =0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i == m-1 and j==n-1):
                    continue
                if (i !=0 or j !=0):
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])+dungeon[i][j]
                    if (dp[i][j] > 0):
                        dp[i][j] = 0
                else:
                    curMax = max(dp[i+1][j],dp[i][j+1])                    
                    if (curMax>0):
                       curMax = 0
                    temp = curMax+dungeon[0][0]
                    dp[0][0] = 1 if temp > 0 else abs(temp)+1
        
        return dp[0][0]

if __name__ == '__main__':
    dungeon = DungeonGame()
    testInput = [[[1],[-2],[1]], [[-2,-3,3],[-5,-10,1],[10,30,-5]],[[-1,1]],[[100]]]
    testResult=[2,7,2,1]

    n = len(testInput)
    for i in range(n):
        result=dungeon.calculateMinimumHP(testInput[i])
        print("Input={}\t\texpected={}\t\tresult={}\t\tmatch={}".format(testInput[i],testResult[i],result,testResult[i] == result))
                    
