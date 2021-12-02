from typing import List
def solveNQueens(n: int) -> List[List[str]]:
        if (n == 1):
            return [["Q"]]
        if (n == 2):
            return []
        ans = []
              
        listStr = []
        
        def printAns()->List[str]:
            temp=[]
            for i1 in range(n):
                temp.append(["."]*n)
            temp2=[]
            for i1 in range(n):
                for j1 in range(n):
                    if ([i1,j1] in ans):
                        temp[i1][j1] = "Q"
                temp2.append("".join(temp[i1]))
            return temp2
       
        def getColQueue(i: int)->List[int]:
            temp = [k for k in range(n)]
            if (len(ans)==0):
                return temp
            else:
                for j in range(i):
                    if (ans[j][1] in temp):
                        temp.remove(ans[j][1])
                    if (ans[j][1]+(i-j) in temp):                   
                        temp.remove(ans[j][1]+(i-j))
                    if (ans[j][1]-(i-j) in temp):
                        temp.remove(ans[j][1]-(i-j))
            return temp
        def putQueeen(i:int):
            nonlocal ans
            if (i==0):
                ans=[]           
            if (i == n):
                listStr.append(printAns())                  
                return
            tempQ = getColQueue(i)
            if (len(tempQ)==0):
                return 
            for j in tempQ:
                ans.append([i,j])
                putQueeen(i+1)                    
                ans.remove([i,j])
            return

                    
        putQueeen(0)
        print(listStr)    


        
            
        return listStr
solveNQueens(4)