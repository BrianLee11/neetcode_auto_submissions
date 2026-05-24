class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}

        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] += 1
        
        for number in dictionary:
            if dictionary[number] == 1:
                return number