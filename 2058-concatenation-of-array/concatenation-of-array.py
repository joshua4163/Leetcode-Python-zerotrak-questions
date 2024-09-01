class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * (2 * n)
        for i in range(n):
            l[i] = nums[i]
            l[i+n] = nums[i]
        return l
            