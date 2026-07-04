from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_shifted = s

        for array in shift:
            k = array[1]

            if array[0] == 0:
                s_shifted = s_shifted[k:] + s_shifted[:k]

            elif array[0] == 1:
                s_shifted = s_shifted[len(s_shifted) - k: len(s_shifted)] + s_shifted[:len(s_shifted) - k]

        return s_shifted



