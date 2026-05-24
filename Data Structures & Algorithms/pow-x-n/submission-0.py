class Solution:
    def myPow(self, x: float, n: int) -> float:


        if n < 0:
            power = -n
        else:
            power = n

        product = 1

        while power > 0:
            product *= x
            power -= 1

        if n < 0:
            product = 1/product

        return product

        




        
        