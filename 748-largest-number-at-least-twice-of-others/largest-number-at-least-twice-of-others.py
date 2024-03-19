class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        z = sorted(nums)
        x = z[-1]
        y = z[-2]
        if x >= y * 2:
            return nums.index(x)
        else:
            return -1