class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        visited = set()

        for number in nums:
            if number not in visited:
                visited.add(number)
            else:
                return number