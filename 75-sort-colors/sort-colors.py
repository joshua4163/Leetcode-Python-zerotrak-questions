class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n - 1
        m = 0
        while m <= r:
            if nums[m] == 2:
                nums[m],nums[r] = nums[r],nums[m]
                r -= 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 0:
                nums[m],nums[l] = nums[l],nums[m]
                l += 1
                m += 1
        return nums