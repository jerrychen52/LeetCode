from typing import List
def QuickSort(arr: List[int]):
    def GetPivot(arr:List[int],lo:int, high:int)->int:
        pivot = arr[high]
        pIndex=high
        i = lo
        while (i < pIndex):
            curNum = arr[i]
            if (curNum > pivot):
                arr[pIndex] = curNum
                arr[i] = arr[pIndex-1]
                arr[pIndex-1]=pivot
                pIndex-=1
            else:
                i+=1
        return pIndex
    def QuickSortSub(arr:List[int],lo:int, high:int):
        if (lo>=high):
            return
        pIndex=GetPivot(arr,lo,high)
        QuickSortSub(arr,lo,pIndex-1)
        QuickSortSub(arr,pIndex+1,high)
    
    QuickSortSub(arr,0,len(arr)-1)

arr = [3,7,8,5,2,1,9,5,4]
QuickSort(arr)
print(arr)