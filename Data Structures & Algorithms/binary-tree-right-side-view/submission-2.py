# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []

        node_array = [root]
        rightMost_values = [root.val]

        while len(node_array) != 0:
            children_node_array = []
            for node in node_array:
                if node.left:
                    children_node_array.append(node.left)
                if node.right:
                    children_node_array.append(node.right)
            
            if children_node_array:
                rightMost_values.append(children_node_array[-1].val)
            
            node_array = children_node_array
        

        return rightMost_values



            





