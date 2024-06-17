class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l =0 
        r = int(sqrt(c))

        while l<=r:
            currsum = l * l + r * r
            if currsum == c:
                return True
            elif currsum <c:
                l += 1
            else:
                r -= 1
        return False