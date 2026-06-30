from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_queue = deque(s)
        target_string = t

        while s_queue:
            target_element = s_queue.popleft()

            try:
                target_element_location_in_t = target_string.index(target_element)
                target_string = target_string[target_element_location_in_t + 1:]
            except:
                return False

        return True