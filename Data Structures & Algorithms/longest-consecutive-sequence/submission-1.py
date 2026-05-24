class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mySet = set(nums)

        # check the beginning of the sequence
        maxCount = 0
        for number in mySet:
            if (number-1) not in mySet:
                count = 1
                targetNumber = number + 1
                
                while targetNumber in mySet:
                    targetNumber += 1
                    count += 1

                maxCount = max(maxCount, count)
                
        return maxCount
            