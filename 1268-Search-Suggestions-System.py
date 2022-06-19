class Node:
    def __init__(self):
        # map: char -> Node
        self.children = {}
        
        # is_end -> True if node is last letter of word
        self.is_end = False
        
        # keys of children
        self.inorder_keys = []
        self.size = 0
        
    def has(self, key: str) -> bool:
        return key in self.children
    
    def _best_index(self, key: str) -> int:
        # use binary search to find insert position of new key
        # we using this approach instead of re-sorting the entire inorder_keys every time
        left, right = 0, self.size - 1
        while left <= right:
            mid = (left + right) >> 1
            val = self.inorder_keys[mid]
            if val < key:
                left = mid + 1
                continue
            if val > key:
                right = mid - 1
                continue
            return mid
        return left
    
    def _add(self, key: str, child: "Node") -> "Node":
        # find lexi inorder spot to insert new key
        self.inorder_keys.insert(self._best_index(key), key)
        self.size+= 1
        
        # map key to child
        self.children[key] = child
        return child
        
    def get_or_create(self, key: str) -> "Node":
        # return child if a mapping exists
        if self.has(key):
            return self.children[key]
        
        # else create a mapping and return that instead
        return self._add(key, Node())

class Solution:
    def _dfs(self, node: "Node") -> List["Node"]:
        # DFS by exploring in lexi order
        # stop immediately on the first 3 end nodes found
        cap = 3
        queue = [node]
        result = []
        while len(queue) > 0:
            v = queue.pop(0)
            if v.is_end:
                result.append(v)
                cap-= 1
                if cap < 1:
                    break
            for c in v.inorder_keys[::-1]:
                queue.insert(0, v.children[c])
        return result
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # root of word Tree
        root = Node()
        
        # map will help us translate node into word
        word_map = {}
        for w in products:
            # add word to tree
            node = root
            for c in w:
                node = node.get_or_create(c)
            node.is_end = True
            
            # map end node to word
            word_map[node] = w
        
        
        result = []
        for c in searchWord:
            # if there is no root, then there is no path in tree
            if root == None:
                result.append([])
                continue
            if not root.has(c):
                root = None
                result.append([])
                continue
                
            # go down the tree if path exist
            root = root.children[c]
            
            # use dfs to find first 3 end nodes
            # use word_map to convert nodes into words
            result.append([word_map[v] for v in self._dfs(root)])
        return result
    
