"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        def bfs(root):
            qu = [root]
            while qu:
                curr_list = []
                for _ in range(len(qu)):
                    front = qu.pop(0)
                    curr_list.append(front.val)
                    for child in front.children:
                        qu.append(child)
                result.append(curr_list)        

        if root:
            bfs(root)
            return result
        else:
            return []    
        