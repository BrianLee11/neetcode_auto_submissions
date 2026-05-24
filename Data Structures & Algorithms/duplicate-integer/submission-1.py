class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         # initialize a dictionary to store key-value
         # key would be a number in nums
         # value would be the frequency of key(number)
         # time complexity: O(1), as a constant operation
        dictionary = {}

        # construct key-value of the dictionary
        # if number exists in dictionary's keys, increment its value by 1
        # if number does not exist in keys, initialize its value by 1
        # time complexity: O(n), where n = nubmer of elements in the nums, since visiting every element in the nums
        for number in nums:
            if number in dictionary:
                dictionary[number] += 1
            else:
                dictionary[number] = 1
        
        # initialize a list to store values of dictionary
        list_dictionary = list(dictionary.values())

        # discover whether frequency larger than or equal to 1 exist in the list
        # true whether value larger than 1 is found
        # false otherwise
        for value in list_dictionary: 
            if value > 1:
                return True

        return False 


