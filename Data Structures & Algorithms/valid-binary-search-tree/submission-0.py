# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        """
        :type root: TreeNode
        :rtype: bool
        """        
        if root == None:
            return True
        
        # print all nodes of the root
                
        def collectAllNodes(node, array):
            if node == None:
                return
            else:
                array.append(node.val)
                collectAllNodes(node.left, array)                
                collectAllNodes(node.right, array)
                
            return array
        
        def checkValuesLeft(node_val, array):
            if array == None:
                return True
            else:
                for value in array:
                    if value >= node_val:
                        return False
                return True

        def checkValuesRight(node_val, array):
            if array == None:
                return True
            else:
                for value in array:
                    if value <= node_val:
                        return False
                return True
        
        def compareValues(node):
            if node == None:
                return True
            
            else:                
                left_values = collectAllNodes(node.left, [])            
                right_values = collectAllNodes(node.right, [])
                
                if checkValuesLeft(node.val, left_values) and checkValuesRight(node.val, right_values):
                    return compareValues(node.left) and compareValues(node.right)
                else:
                    return False
       
        return compareValues(root)
        
        