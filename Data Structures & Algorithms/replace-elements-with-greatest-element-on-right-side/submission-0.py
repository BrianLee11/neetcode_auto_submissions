from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length_arr = len(arr)

        if length_arr == 1:
            return [-1]

        elif length_arr == 2:
            return [arr[-1], -1]

        else:
            sorted_arr = [""] * length_arr
            sorted_arr[length_arr - 1] = -1
            sorted_arr[length_arr - 2] = arr[-1]

            current_max_number = arr[-1]
            for index in range(length_arr - 3, -1, -1):
                target_number = arr[index + 1]
                if target_number > current_max_number:
                    current_max_number = target_number
                sorted_arr[index] = current_max_number

            return sorted_arr
