class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum < target:
                ans += (r - l)
                l += 1
            else:
                r -= 1
        return ans