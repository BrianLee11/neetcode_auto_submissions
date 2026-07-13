from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        queue = deque()
        int_sum = 0

        for element in operations:
            if element == '+':
                int_second_number = queue.pop()
                int_first_number = queue.pop()
                int_operated_two_number = int_first_number + int_second_number

                queue.append(int_first_number)
                queue.append(int_second_number)
                queue.append(int_operated_two_number)
                int_sum += int_operated_two_number

            elif element == 'D':
                int_first_number = queue.pop()

                int_operated_two_number = 2 * int_first_number
                int_sum += int_operated_two_number

                queue.append(int_first_number)
                queue.append(int_operated_two_number)

            elif element == 'C':
                int_remove_number = queue.pop()
                int_sum -= int_remove_number

            else:
                int_element = int(element)
                queue.append(int_element)
                int_sum += int_element

        return int_sum
