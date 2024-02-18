class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        large = 0
        maxindcies = (0,0)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[i] * nums[j]
                if x>large:
                    large = x
                    maxindcies = (i,j)
                    y = (nums[i]-1)*(nums[j]-1)
        return y
        