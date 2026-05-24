class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}

        for index in range(len(nums)):
            supplement = target - nums[index]

            if supplement in dictionary: 
                return [dictionary[supplement], index]
            else:
                dictionary[nums[index]] = index
        
            

