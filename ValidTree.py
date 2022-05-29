from typing import (
    List,
)

class ValidTree:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        adj = {}
        for edge in edges:
            if (not (edge[0] in adj.keys())):
                adj[edge[0]] = set()
            adj[edge[0]].add(edge[1])
            if (not (edge[1] in adj.keys())):
                adj[edge[1]] = set()
            adj[edge[1]].add(edge[0])
        
        visit = {}
        res=[]
        def dfs(i):
            if (i in visit):
                return visit[i]
            visit[i]=True
            if (i in adj.keys()):
                for neighbor in adj[i]:
                    if (dfs(neighbor)):
                        return True
            visit[i] = False
            res.append(i)
            return False
        
        for i in range(n):
            if (dfs(i)):
                return False
        
        if len(res)!= n:
            return False
        return True

if __name__ == '__main__':
    valid=ValidTree()
    inputs = [[5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
    [5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
        
    ]
    results = [True,False]

    for i in range(len(inputs)):
        input =inputs[i]
        res = valid.valid_tree(input[0],input[1])
        print("input={} result={} expect={} match={}".format(input,res,results[i],res==results[i]))
