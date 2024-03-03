class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        product = 1
        summation = 0
        
        for digit in digits:
            product *= digit
            summation += digit
            
        return product - summation
