class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def has(self, key: str) -> bool:
        return key in self.children
    
    def get_or_create(self, key: str) -> "Node":
        if self.has(key):
            return self.children[key]
        child = Node()
        self.children[key] = child
        return child
    
class WordTree:
    def __init__(self):
        self.root = Node()
    
    def add(self, word: str) -> "Node":
        node = self.root
        for c in word:
            node = node.get_or_create(c)
        return node

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # build suffix tree
        suffix_tree = WordTree()
        # map node -> word length
        node_lens = {}
        for w in words:
            node_lens[suffix_tree.add(w[::-1])] = len(w)
            
        # word A can only be encoded into word B
        # if A is a suffix of B
        # if not, they are treated as seperate words
        # all required words are the leafs
        total = 0
        for v, l in node_lens.items():
            if len(v.children) > 0:
                continue
            total+= 1 + l
        return total
      
