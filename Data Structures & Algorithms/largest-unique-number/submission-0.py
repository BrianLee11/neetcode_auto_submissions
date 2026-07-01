from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for number in nums:
            if number in dictionary:
                dictionary[number] = True
            else:
                dictionary[number] = False

        try:
            max_only_occur_once = max([key for key, value in dictionary.items() if value == False])
            return max_only_occur_once
        except:
            return -1