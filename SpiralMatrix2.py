from typing import List
def generateMatrix(n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(j)
            ans.append(row)
        
        rowBegin=0
        rowEnd = n-1
        colBegin=0
        colEnd=n-1
        
        current=0
        while (rowBegin<=rowEnd and colBegin<=colEnd):
            for i in range(colBegin,colEnd+1,1):
                current+=1
                ans[rowBegin][i] = current
            rowBegin+=1
            
            for i in range(rowBegin,rowEnd+1,1):
                current+=1
                ans[i][colEnd] = current
            colEnd-=1
            
            for i in range(colEnd,colBegin-1,-1):
                current+=1
                ans[rowEnd][i]=current
            
            rowEnd-=1
            
            for i in range(rowEnd,rowBegin-1,-1):
                current+=1
                ans[i][colBegin]=current
            
            colBegin+=1
        
        return ans

l = generateMatrix(4)
l


