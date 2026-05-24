class Solution(object):

    class ListNode():
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        linkedLists = list(lists)
        output_array = []

        while linkedLists:
            minValue = None
            minIndex = -1

            for i in range(len(linkedLists)):
                current = linkedLists[i]
                if current is None:
                    continue
                if minValue is None or current.val < minValue.val:
                    minValue = current
                    minIndex = i

            if minValue is None:
                break

            output_array.append(minValue)
            linkedLists[minIndex] = linkedLists[minIndex].next

            linkedLists = [node for node in linkedLists if node is not None]

        if not output_array:
            return None

        # connect nodes in the output_array
        head = output_array[0]
        current = head

        for node in output_array[1:]:
            current.next = node
            current = current.next

        return head