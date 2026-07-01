from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary_num2_index_location = {}
        for index in range(len(nums2)):
            if nums2[index] not in dictionary_num2_index_location:
                dictionary_num2_index_location[nums2[index]] = index

        array_nums1_index_loaction = []

        for number in nums1:
            array_nums1_index_loaction.append(dictionary_num2_index_location[number])

        return array_nums1_index_loaction
