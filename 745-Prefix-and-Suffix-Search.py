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
    
    def store(self, i: int):
        self.refs.add(i)
        
class WordTree:
    def __init__(self):
        self.counter = 0
        self.refs = {}
        self.root = LetterNode()
        
    def add(self, word: str, rep: int) -> "LetterNode":
        if len(word) < 1:
            return None
        
        # create a mapping between the counter and rep
        self.refs[self.counter] = rep
        
        # iterate through the tree with each letter sequentially
        node = self.root
        for c in word:
            node = node.get(c)
            
            # store word reference into each node
            node.store(self.counter)
            
        # increment counter for future word
        self.counter+= 1
        
        return node
    
    def findNode(self, prefix: str) -> "LetterNode":
        if len(prefix) < 1:
            return None
        
        # iterate through the tree
        node = self.root
        for c in prefix:
            # return None on first instance of no letter found
            if not node.has(c):
                return None
            node = node.get(c)
        return node
    
    def translateRefs(self, node: "LetterNode") -> Set[int]:
        # node.refs does not actually contain the word indexes
        # the word indexes were replaced with different counter IDs assigned by the tree
        # this translate the tree IDs back into the original word indexes
        return set([self.refs[i] for i in list(node.refs)])
    
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
        a = self.start.findNode(prefix)
        b = self.end.findNode(suffix[::-1])
        if a == None or b == None:
            return -1
        
        # find all common word references between prefix and suffix node
        a_refs = self.start.translateRefs(a)
        b_refs = self.end.translateRefs(b)
        common_refs = list(a_refs & b_refs)
        if len(common_refs) < 1:
            return -1
        
        # get biggest index
        common_refs.sort()
        return common_refs[-1]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
