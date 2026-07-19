from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_occurrence_1 = 0
        current_occurrence_1 = 0

        for number in nums:
            if number == 0:
                current_occurrence_1 = 0
            else:
                current_occurrence_1 += 1

                # update the max
                if current_occurrence_1 > max_occurrence_1:
                    max_occurrence_1 = current_occurrence_1

        return max_occurrence_1
