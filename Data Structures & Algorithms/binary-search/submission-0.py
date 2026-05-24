class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        else:
            leftIndex = 0
            rightIndex = len(nums) -1

            while (leftIndex <= rightIndex):
                midIndex = (leftIndex + rightIndex) // 2

                # Found
                if nums[midIndex] == target:
                    return midIndex
                
                # Not found. nums[midIndex] < target
                # left part is omitted. consider the right part only
                elif nums[midIndex] < target:
                    leftIndex = midIndex + 1


                # Not found. nums[midIndex] > target
                # right part is omitted. consider the left part only
                else:
                    rightIndex = midIndex - 1