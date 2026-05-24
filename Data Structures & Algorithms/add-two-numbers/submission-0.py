# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listNodeToInteger(listNode):
            
            power = 0
            current = listNode
            total = 0
            
            while current:
                
                digit = current.val
                total += digit * (10**power)
                power += 1
                
                current = current.next
                
            return total
        
        target_integer = listNodeToInteger(l1) + listNodeToInteger(l2)
        
        def integerToListNode(target_integer):
            head = ListNode(target_integer%10)
            current_node = head
            target_integer //= 10
            
            while target_integer > 0:
                next_node = ListNode(target_integer%10)
                current_node.next = next_node            
                current_node = next_node
                
                target_integer //= 10

            return head
        
        
        return integerToListNode(target_integer)        