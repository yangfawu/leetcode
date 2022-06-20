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
      
