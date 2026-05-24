class Solution(object):
    
    
    def isHappy(self, n: int) -> bool:
        dictionary = {}
    
        def addSumOfSquares(n):
            total = 0
            while n >= 1:
                digit = n % 10
                total += digit ** 2
                n //= 10
    
            return total
        
        summation = addSumOfSquares(n)
        if summation == 1:
            return True

        while summation != 1:
            
            summation = addSumOfSquares(summation)
            
            if summation == 1:
                return True
            
            if summation in dictionary:
                return False
            else:
                dictionary[summation] = 1