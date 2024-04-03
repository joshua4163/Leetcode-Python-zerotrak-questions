class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        List = []
        l = 0
        nums.sort()
        # [0,1,3,4,4,5]
        r = len(nums) - 1

        while l < r:
            List.append((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(set(List))