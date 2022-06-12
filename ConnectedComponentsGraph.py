'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find 
the number of connected components in an undirected graph.
Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
     0          3
     |          |
     1 --- 2    4 
Output: 2
Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
     0           4
     |           |
     1 --- 2 --- 3
Output:  1
Note:
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and 
thus will not appear together in edges.
'''
from typing import List

def numConnected(n:int, edges:List[List[int]])->int:
    parent = [*range(n)]
    rank = [1]*n 

    def find(n1):
        res = parent[n1]
        if res!=parent[res]:
            res=find(parent[res])            
        '''while (res !=parent[res]):
            parent[res]=parent[parent[res]] #path compression
            res=parent[res] 
           '''
        parent[n1] = res
        return res
    
    def union(n1,n2):
        p1=find(n1)
        p2=find(n2)
        if (p1==p2):
            return 0
        if (rank[p1]>rank[p2]):
            parent[p2]=p1
            rank[p1]+=1
        else:
            parent[p1]=p2
            rank[p2]+=1
        return 1 # remove one parent
    ans = n
    for edge in edges:
        e1=edge[0]
        e2=edge[1]
        ans -= union(e1,e2)
    return ans


if __name__ == '__main__':
    inputs = [
       [5, [[0, 1], [1, 2], [3, 4]]],
       [5, [[0, 1], [1, 2], [2, 3], [3, 4]]]
    ]

    outputs=[2,1]

    for i in range(len(inputs)):
        input = inputs[i]
        ans= numConnected(input[0],input[1])
        print("input={} ans={} expected={} match={}".format(input,ans,outputs[i],ans==outputs[i]))
        

        
        