class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if (head is None or head.next is None):
            return head
        def merge(head1, head2):
            dummy = Node(0)
            curNode = dummy
            node1=head1
            node2=head2
            while (not(head1 is None) or not (head2 is None)):
                if (node1 is None or node1.data>node2.data):
                    curNode.next=node2
                    node2=node2.next
                elif (node2 is None or node2.data>node1.data):
                    curNode.next=node1
                    node1=node1.next
                curNode=curNode.next
            
            return dummy.next
        
        def split(head):
            if (head is None or head.next is None):
                return head
            fast = head
            slow = head
            prev = None
            while (not(fast is None or fast.next is None)):
                prev = slow
                fast = fast.next.next
                slow = slow.next
            
            prev.next = None
            return slow
        
        tail = split(head)
        node1 = self.mergeSort(head)
        node2 = self.mergeSort(tail)
        return merge(node1,node2)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        #n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends