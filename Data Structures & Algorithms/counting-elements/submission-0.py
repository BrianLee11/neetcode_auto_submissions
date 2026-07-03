from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        set_arr = set(arr)
        output_count = 0

        for number in arr:
            if (number + 1) in set_arr:
                output_count += 1

        return output_count