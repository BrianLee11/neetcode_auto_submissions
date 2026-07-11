# convert to a function
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        int_distance_from_start = 0 # initialization

        for log in logs:
            # ../ means move to the parent folder of the current folder
            if log == "../":
                # if already in the main folder, reamin in the same folder
                if int_distance_from_start == 0:
                    continue
                else:
                    int_distance_from_start -= 1

            # ./ means stay in the same folder
            elif log == "./":
                # do nothing. move to the next log.
                continue

            # x/ means other than ../ and ./, we are visiting x folder
            else:
                int_distance_from_start += 1

        return int_distance_from_start