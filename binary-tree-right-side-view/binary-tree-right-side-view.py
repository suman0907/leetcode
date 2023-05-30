# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def bfs(root):
            qu = [root]
            while qu:
                curr_list = []
                for _ in range(len(qu)):
                    front = qu.pop(0)
                    curr_list.append(front.val)
                    if front.left:
                        qu.append(front.left)
                    if front.right:
                        qu.append(front.right)
                result.append(curr_list[-1])
        if root:
            bfs(root)
            return result
        else:
            return []                        
        