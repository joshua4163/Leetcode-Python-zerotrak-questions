class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max1 = max(nums)
        min1 = min(nums)
        for n in nums:
            if n != max1 and n != min1:
                return n
        return -1