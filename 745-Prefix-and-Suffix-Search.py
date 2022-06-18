class LetterNode:
    def __init__(self):
        self.children = {}
        self.refs = set()
    
    def has(self, c: str) -> bool:
        return c in self.children
    
    def get(self, c: str) -> "LetterNode":
        # if child exist, return it
        if self.has(c):
            return self.children[c]
        
        # else create it and add it
        child = LetterNode()
        self.children[c] = child
        return child
    
    def add_ref(self, i: int):
        self.refs.add(i)
        
class WordTree:
    def __init__(self):
        self.root = LetterNode()
        
    def add(self, word: str, rep: int) -> "LetterNode":
        # iterate through the tree with each letter sequentially
        node = self.root
        for c in word:
            node = node.get(c)
            # store word reference into each node
            node.add_ref(rep)
        
        return node
    
    def find_node(self, prefix: str) -> "LetterNode":
        # iterate through the tree
        node = self.root
        for c in prefix:
            # return root on first instance of no letter found
            if not node.has(c):
                return self.root
            node = node.get(c)
        return node
    
class WordFilter:
    def __init__(self, words: List[str]):
        # create 2 roots
        # 1 for prefix searching
        # 1 for suffix searching
        self.start = WordTree()
        self.end = WordTree()
        for i, w in enumerate(words):
            self.start.add(w, i)
            self.end.add(w[::-1], i)

    @cache
    def f(self, prefix: str, suffix: str) -> int:
        # find letter nodes of prefix and suffix
        a = self.start.find_node(prefix)
        b = self.end.find_node(suffix[::-1])
        
        # find all common word references between prefix and suffix node
        # get biggest index
        # default is -1 if no common found
        common_refs = a.refs & b.refs
        common_refs.add(-1)
        return max(common_refs)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
