class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_len = float('inf')
        for r in range(len(nums) - k + 1):
            x = nums[r+k-1] - nums[r]
            min_len = min(min_len,x)
        return min_len