from typing import List

def search(nums: List[int], target: int) -> int:
        def findPivot()->int:
            left = 0
            right = len(nums)-1
            while (left<right):
                mid = left + (right-left) // 2
                print("left={} right={} mid={} nums[mid]={}".format(left,right,mid,nums[mid]))
                if (nums[mid]>nums[right]):
                    left = mid+1
                else:
                    right=mid
            
            return left
        
        def binarySearch(start:int, end:int,  target:int)->int:
            while (start <end):
                mid = start+(end-start) // 2
                if (nums[mid] == target):
                    return mid
                if (nums[mid]>target):
                    end = mid-1
                else:
                    start=mid+1
            
            return -1
        
        pivot = findPivot()
        print("pivot={}".format(pivot))
        start = 0
        end = len(nums)-1
        if (target >=pivot and target<=nums[end]):
            start = pivot
        else:
            end = pivot-1
        return binarySearch(start,end,target)
           
search([4,5,6,7,0,1,2],0)
