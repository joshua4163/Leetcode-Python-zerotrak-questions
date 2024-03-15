class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small = nums[0]
        large = nums[-1]
        while(large):
            small , large = large, small % large
        return abs(small)