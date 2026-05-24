class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}

        for index in range(len(numbers)):
            reciprocal = target - numbers[index]

            if reciprocal in dictionary:
                return [dictionary[reciprocal] + 1, index + 1]

            else:
                dictionary[numbers[index]] = index

