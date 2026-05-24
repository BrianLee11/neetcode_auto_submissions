class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(numerator, denominator):
            return (numerator + denominator - 1) // denominator
        
        left, right = 1, max(piles)
        
        while left < right:
            speed = (left + right) // 2
            elapsed_time = sum(ceil(pile, speed) for pile in piles)
            
            if elapsed_time > h:
                left = speed + 1
            else:
                right = speed
                
        return left    