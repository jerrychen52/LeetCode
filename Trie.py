class Trie:
    class Node:
        def __init__(self,c:chr) -> None:
            self.curChar = c
            self.end = 0
            self.children = {}
        def insert(self,c:chr):
            if (not(c in self.children.keys())):
                self.children[c] = Trie.Node(c)
        def setEnd(self):
            self.end+=1
        def contains(self,c:chr)->bool:
            if (c in self.children.keys()):
                return True
            return False
    
    def __init__(self):
        self.root = Trie.Node('/')

    def insert(self, word: str) -> None:
        cur = self.root
        n = len(word)
        for i in range(n):
            c = word[i]
            cur.insert(c)            
            cur = cur.children[c]
            if (i == n-1):
                cur.setEnd()

    def findLastNode(self,word:str)->Node:
        n = len(word)
        cur = self.root
        for i in range(n):
            c = word[i]
            if (not(c in cur.children.keys())):
                return None
            cur = cur.children[c]
        return cur

    def search(self, word: str) -> bool:
        lastNode = self.findLastNode(word)
        if (lastNode is None or lastNode.end == 0):
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        if (self.findLastNode(prefix) is None):
            return False
        return True
    
    
if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print("search apple={}".format(trie.search("apple"))) # should be True
    print("search app={}".format(trie.search("app"))) # should #be False
    print("start with app ={}".format(trie.startsWith("app"))) # return True
    trie.insert("app")
    print("search app={}".format(trie.search("app"))) # should #be true

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)