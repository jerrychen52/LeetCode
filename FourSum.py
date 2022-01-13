from typing import List
class FourSum:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                rem = target - (nums[i]+nums[j])
                p1 = j+1
                p2 = n-1
                while (p1<p2):
                    if (nums[p1]+nums[p2]<rem):
                        p1+=1
                        continue
                    elif (nums[p1]+nums[p2]>rem):
                        p2-=1
                        continue
                    else:
                        ans.append([nums[i],nums[j],nums[p1],nums[p2]])
                        if (nums[p1]==nums[p2]):
                            break
                        while (p1<p2 and nums[p1+1]==nums[p1]):
                            p1+=1
                        while (p1<p2 and nums[p2-1] == nums[p2]):
                            p2-=1
                        p1+=1
                        p2-=1
        
        return ans

if __name__ == '__main__':
    four = FourSum()
    print(four.fourSum([1,0,-1,0,-2,2],0))