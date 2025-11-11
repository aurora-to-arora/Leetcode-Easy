"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        def helper(node):
            if node:
                res.append(node.val)
                for i in node.children:
                    helper(i)
        helper(root)
        return res


#can I make it better?
