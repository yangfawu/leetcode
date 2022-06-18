class LetterNode:
    def __init__(self, p: "LetterNode", c: str):
        self.val = c
        self.parent = p
        self.children = {}
        self.refs = set()
    
    def has(self, c: str) -> bool:
        return c in self.children
    
    def get(self, c: str) -> "LetterNode":
        if self.has(c):
            return self.children[c]
        child = LetterNode(self, c)
        self.children[c] = child
        return child
    
    def store(self, i: int):
        self.refs.add(i)
        
class WordTree:
    def __init__(self):
        self.counter = 0
        self.refs = {}
        self.root = LetterNode(None, "_")
        
    def add(self, word: str, rep: int) -> "LetterNode":
        if len(word) < 1:
            return None
        self.refs[self.counter] = rep
        node = self.root
        for c in word:
            node = node.get(c)
            node.store(self.counter)
        self.counter+= 1
        return node
    
    def readRefs(self, refs: List[int]) -> List[int]:
        return [self.refs[r] for r in refs]
    
    def findNode(self, prefix: str) -> "LetterNode":
        if len(prefix) < 1:
            return None
        node = self.root
        for c in prefix:
            if not node.has(c):
                return None
            node = node.get(c)
        return node
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.start = WordTree()
        self.end = WordTree()
        for i, w in enumerate(words):
            self.start.add(w, i)
            self.end.add(w[::-1], i)

    @cache
    def f(self, prefix: str, suffix: str) -> int:
        a = self.start.findNode(prefix)
        b = self.end.findNode(suffix[::-1])
        if a == None or b == None:
            return -1
        a_refs = self.start.readRefs(list(a.refs))
        b_refs = self.end.readRefs(list(b.refs))
        refs = list(set(a_refs) & set(b_refs))
        if len(refs) < 1:
            return -1
        refs.sort(reverse=True)
        return refs[0]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
