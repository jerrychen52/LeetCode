from typing import List
def canPartitionKSubsets(nums: List[int], k: int) -> bool:
        if (len(nums)<k):
            return False
        totalSum=sum(nums)
        if (totalSum % k!=0):
            return False
        groupSum = totalSum //k
        n = len(nums)
        usedSet=set()     
        
        def tryGroup(curNumGroup:int, curSum:int)->bool:
            if (curNumGroup==k):
                return len(usedSet)==n
            
            for i in range(n):
                if (not (i in usedSet)):
                    temp = curSum+nums[i]
                    if (temp>groupSum):
                        break
                    if (temp == groupSum):
                        usedSet.add(i)
                        if (tryGroup(curNumGroup+1,0)):
                            return True
                        else:
                            usedSet.remove(i)
                    else:
                        usedSet.add(i)
                        if (tryGroup(curNumGroup,temp)):
                            return True
                        else:
                            usedSet.remove(i)
            
            return False
        
        if (tryGroup(0,0)):
            return True

#canPartitionKSubsets([4,3,2,3,5,2,1],4)
print(canPartitionKSubsets([18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037],4))