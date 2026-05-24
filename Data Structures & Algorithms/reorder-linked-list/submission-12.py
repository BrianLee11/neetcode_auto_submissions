class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return  # No need to return the head

        array = []
        current_node = head
        
        # Collect all nodes in the array
        while current_node:
            array.append(current_node)
            current_node = current_node.next
        
        current_node = head            
        next_node = current_node.next
        target = array.pop()
        
        # Reordering the list
        while current_node != target:
            current_node.next = target
            target.next = next_node
            
            if array:
                target = array.pop()
                current_node = next_node
                next_node = current_node.next
            
            # Handling the last connections
            if current_node == target:
                current_node.next = None
                break
            if next_node == target:
                next_node.next = None
                break
