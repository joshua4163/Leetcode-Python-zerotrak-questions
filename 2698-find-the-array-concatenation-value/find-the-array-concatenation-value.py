class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        summ = 0
        while l <= r:
            if l == r:
                summ += nums[r]
                break
            else:
                summ += int(str(nums[l]) + str(nums[r]))
                l += 1
                r -= 1
        return summ