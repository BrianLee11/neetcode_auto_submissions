class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arrayLength = len(nums)
        prefixArray = [1] * arrayLength
        suffixArray = [1] * arrayLength
        productArray = [1] * arrayLength

        # prefix array
        for index in range(arrayLength):
            if index == 0:
                prefixArray[index] = 1
            elif index == 1:
                prefixArray[index] = nums[0]
            else:
                prefixArray[index] = prefixArray[index - 1] * nums[index-1]
        
        # suffix array
        for index in range(arrayLength - 1, -1, -1):
            if index == arrayLength - 1:
                suffixArray[index] = 1
            elif index == arrayLength -2:
                suffixArray[index] = nums[index + 1]
            else:
                suffixArray[index] = suffixArray[index + 1] * nums[index + 1]
        
        # product array
        for index in range(arrayLength):
            productArray[index] = prefixArray[index] * suffixArray[index]

        return productArray

            
