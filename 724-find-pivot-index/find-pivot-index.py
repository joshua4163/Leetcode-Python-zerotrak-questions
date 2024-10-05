class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)
        leftsum = 0 
        for i in range(n):
            rightsum = totalsum - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1  # Return -1 if no pivot index is found
