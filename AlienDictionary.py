'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Solution: Toplogical sort (If cycle is detected then no answer.)
'''
from typing import List
def alienOrder(words:List[str])->str:
    adj = {c:set() for w in words for c in w }
    for i in range(len(words)-1):
        w1,w2 = words[i], words[i+1]
        minLen = min(len(w1),len(w2))   
        if (len(w1) > len(w2) and w1[:minLen]==w2[:minLen]):
            return ""   
        for j in range(minLen):
            if (w1[j]!=w2[j]):
                adj[w1[j]].add(w2[j])
                break    
    visit = {} # False = visited, True= in path
    res = []

    def dfs(c):
        #print("c={}".format(c))
        if c in visit:
            return visit[c]
        visit[c] = True
        for neighbor in adj[c]:
            if (dfs(neighbor)):
                return True

        visit[c] = False
        print("c={} res={}".format(c,res))
        res.append(c)
        return False

    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)

if __name__ == '__main__':
    input=[["wrt",  "wrf",  "er",  "ett",  "rftt"], ["z","x","z"]]
    output=["wertf", ""]
    for i in range(len(input)):
        words= input[i]
        retval = alienOrder(words)
        print("Input={} output={} expected={} match={}".format(words,retval,output[i], retval==output[i]))