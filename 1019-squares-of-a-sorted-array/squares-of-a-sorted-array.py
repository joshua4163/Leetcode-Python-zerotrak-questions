class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        y = []
        for i in range(len(nums)):
            x = nums[i] * nums[i]
            y.append(x)
            y.sort()
        return y

        