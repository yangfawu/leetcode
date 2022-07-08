# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # bfs all nodes
        # ordered from top to bottom, left to right
        nodes = []
        queue = [root]
        while len(queue):
            n = queue.pop(0)
            if n == None:
                continue
            nodes.append(n)
            queue.append(n.left)
            queue.append(n.right)
        
        # compute tilt value leaf-first to root
        total = 0
        while len(nodes):
            n = nodes.pop()
            left = 0 if n.left == None else n.left.val
            right = 0 if n.right == None else n.right.val
            n.val+= left
            n.val+= right
            total+= abs(left - right)
        
        return total
      
