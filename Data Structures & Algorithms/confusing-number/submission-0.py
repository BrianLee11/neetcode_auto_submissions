from collections import deque

class Solution:
    def confusingNumber(self, n: int) -> bool:
        n_str = str(n)

        invalid_chars = {"2", "3", "4", "5", "7"}
        rotation_dictionary = {"0": "0",
                               "1": "1",
                               "6": "9",
                               "8": "8",
                               "9": "6"}

        rotated_number_queue = deque()
        for character in n_str:
            if character in invalid_chars:
                return False

            elif character in rotation_dictionary:
                rotated_number_queue.appendleft(rotation_dictionary[character])

        rotated_number_string = ''.join(rotated_number_queue)

        if n_str == rotated_number_string:
            return False

        return True

