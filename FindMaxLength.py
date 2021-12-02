from typing import List
def findMaxLength(nums: List[int]) -> int:
        ans = 0
        count=0
        countMap = dict()
        countMap[0]=-1
        print("countMap[0]=".format(countMap.get(0)))
        for i in range(len(nums)):
            if (nums[i] ==0):
                count-=1
            else:
                count+=1
            print("count={}".format(count))
            if (countMap.get(count,-1)!=-1):
                ans=max(ans,i-countMap.get(count))
            else:
                countMap[count]=i
        
        return ans

findMaxLength([0,1])
