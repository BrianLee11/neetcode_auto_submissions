# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareRoot(p, q):
            if p and not q:
                return False
            elif not p and q:
                return False
            elif not p and not q:
                return True
            else:
                if p.val != q.val:
                    return False
                else:
                    return compareRoot(p.left, q.left) and compareRoot(p.right, q.right)

        ##########################
        output = []
        def findKeyRoot(root, key):
            if root == None:
                return
            else:
                if root.val == key:
                    output.append(root)
                
                findKeyRoot(root.left, key)
                findKeyRoot(root.right, key)
            
            return output
        ##########################
        
        keyLocation = findKeyRoot(p, q.val)
        
        if keyLocation:
            for node in keyLocation:
                if compareRoot(node, q) == True:
                    return True
        
        return False