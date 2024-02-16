class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prefix = 0
        res = 0
        for x in nums:
            prefix += x
            if prefix == 0:
                res += 1
        return res

        