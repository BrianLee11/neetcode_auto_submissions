# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        else:
            root_array = [root]
            output = []

            while root_array != []:
                values = []
                for root in root_array:
                    values.append(root.val)

                output.append(values)

                temp_root_array = []
                for root in root_array:
                    if root.left:
                        temp_root_array.append(root.left)
                    if root.right:
                        temp_root_array.append(root.right)
                
                root_array = temp_root_array
            
            return output
                



