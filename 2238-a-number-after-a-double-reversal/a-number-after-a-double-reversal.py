class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversednum1 = 0
        reversednum2 = 0
        
        # Reversing num to get reversednum1
        temp = num
        while temp != 0:
            digit = temp % 10
            reversednum1 = reversednum1 * 10 + digit
            temp = temp // 10
        
        # Reversing reversednum1 to get reversednum2
        temp = reversednum1
        while temp != 0:
            digit = temp % 10
            reversednum2 = reversednum2 * 10 + digit
            temp = temp // 10
        
        # Comparing reversednum2 with original num
        return reversednum2 == num