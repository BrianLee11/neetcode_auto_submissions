from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:        
        # Do not return anything, modify nums1 in-place instead.
        index_nums1 = 0
        index_nums2 = 0

        move_amount = 0
        while index_nums2 < n:
            while index_nums1 < m + n:
                if nums1[index_nums1] <= nums2[index_nums2]:
                    index_nums1 += 1
                else:
                    for index in range(m + move_amount, index_nums1, -1):
                        nums1[index] = nums1[index - 1]
                    nums1[index_nums1] = nums2[index_nums2]
                    move_amount += 1
                    # print(f"nums1: {nums1}")
                    # print(f"nums2: {nums2}")
                    break

            index_nums2 += 1

        for index in range(n - move_amount):
            nums1[index + move_amount + m] = nums2[index + move_amount]

        return nums1
