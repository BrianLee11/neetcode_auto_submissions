from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index_zero = 0
        index_non_zero = 0
        length_nums = len(nums)

        while index_zero < length_nums and index_non_zero < length_nums:

            # find zero index
            while index_zero < length_nums:
                if nums[index_zero] != 0:
                    index_zero += 1
                    continue
                else:
                    break

            # find non-zero index
            index_non_zero = index_zero + 1

            while index_non_zero < length_nums:
                if nums[index_non_zero] == 0:
                    index_non_zero += 1
                    continue
                else:
                    break

            # swap, if condition is met
            if index_zero < length_nums and index_non_zero < length_nums:
                # swap
                nums[index_zero], nums[index_non_zero] = nums[index_non_zero], nums[index_zero]
                index_zero = + 1

        return nums  # [1, 2, 5, 0, 0, 0]
