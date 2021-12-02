class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        setNum=set()
        curNode= head2
        ans = ""
        while(not(curNode is None)):
            setNum.add(curNode.data)
            curNode = curNode.next
        curNode = head1
        while(not (curNode is None)):
            if (curNode.data in setNum):
                ans+=str(curNode.data)+" "
            curNode=curNode.next
        
        print(ans)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next

if __name__ == '__main__':
    n1 = int(input())
    arr1 = [int(x) for x in input().split()]
    ll1 = linkedList()
    for i in arr1:
        ll1.insert(i)
        
    n2 = int(input())
    arr2 = [int(x) for x in input().split()]
    ll2 = linkedList()
    for i in arr2:
        ll2.insert(i)
        
    result = Solution().findIntersection(ll1.head,ll2.head)
    printList(result)
    print()
        
     

