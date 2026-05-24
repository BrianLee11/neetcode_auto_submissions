class Solution:
        
    def twoSum(self, nums, target):
        dictionary = {}
        output_array = []
        
        for index in range(len(nums)):
            dictionary[nums[index]] = index
        
        for index in range(len(nums)):
            reciprocal = target - nums[index]
            output = []
            
            if reciprocal in dictionary:
                if dictionary[reciprocal] != index:
                    if [dictionary[reciprocal], index].sort() not in output_array:
                        output.append(dictionary[reciprocal])
                        output.append(index)
                        output_array.append(output)
                
        return output_array
    
    
    def threeSum(self, nums):
        output_array = []
        
        for index in range(len(nums)):
            
            target = - nums[index]
            
            coordinates_2D = self.twoSum(nums, target)
        
            if coordinates_2D is not None:
                for coordinate in coordinates_2D:
                    if index not in coordinate:
                        coordinate.append(index)
                        
                        first = coordinate[2]
                        second = coordinate[0]
                        third = coordinate[1]
                        
                        values = []
                        values.append(nums[first])
                        values.append(nums[second])
                        values.append(nums[third])
                        
                        values.sort()
                        
                        if values not in output_array:
                            output_array.append(values)
                                                
        return output_array