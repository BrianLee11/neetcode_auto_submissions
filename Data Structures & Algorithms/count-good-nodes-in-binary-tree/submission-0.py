# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def visitAllNodes(node, path):

            if node == None:
                return 
            
            else:
                add_one = True
                #print(node.val)
                #print(path)
                
                for number in path:
                    if number > node.val:
                        add_one = False
                        break
                    
                if add_one == True:
                    self.count += 1
                #print(self.count)
                #print()
                
                new_path = path + [node.val]
                visitAllNodes(node.left, new_path)
                visitAllNodes(node.right, new_path)
                

        path = []
        visitAllNodes(root, path)
        return self.count
        