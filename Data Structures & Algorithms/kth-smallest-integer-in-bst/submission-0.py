# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        output = []

        def visitAllNodes(node):
            if node == None:
                return
            else:
                output.append(node.val)
                visitAllNodes(node.left)
                visitAllNodes(node.right)
        
        visitAllNodes(root)
        output.sort()

        return output[k-1]
