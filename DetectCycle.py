from typing import List
from ListNode import *
class Solution:
    def detectCycle(self, head:ListNode)->ListNode:
        if (head is None or head.next is None):
            return None
        fast = head.next.next
        slow = head.next
        while (fast!= slow):
            if (fast is None or fast.next is None):
                return None
            fast = fast.next.next
            slow=slow.next
        
        curNode=head
        while (curNode != slow):
            curNode=curNode.next
            if (curNode == slow):
                return slow
            slow= slow.next
        
        return curNode
    
    def createList(self, arr: List[int], pos:int)->ListNode:
        nodes = []
        if (arr is None or len(arr)==0):
            return None
        head = ListNode(arr[0])
        nodes.append(head)
        curNode = head
        n = len(arr)
        i=1
        while (i<n-1):
            curNode.next = ListNode(arr[i])
            nodes.append(curNode)
            curNode = curNode.next
            i+=1            
        curNode.next= ListNode(arr[n-1])
        curNode.next.next = nodes[pos]
        return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':    
    arr1 = [3,2,0,-4]
    n1 = 1
    s = Solution()
    head = s.createList(arr1,n1)
    node = s.detectCycle(head)
    print("Success" if node.val==3 else "Fail")
        
    
    

   
        
