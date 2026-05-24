# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head.next.next == None:
            return 

        array = []
        
        current_node = head
        
        while current_node:
            array.append(current_node)
            current_node= current_node.next
        
        current_node = head            
        next_node = current_node.next

        target = array.pop()
        
        while current_node != target:
            current_node.next = target
            target.next = next_node
            
            if array != []:
                target = array.pop()
                
                current_node = next_node
                next_node = current_node.next
            
            if current_node == target:
                current_node.next = None
                break
                
            if next_node == target:
                next_node.next = None
                break
        
