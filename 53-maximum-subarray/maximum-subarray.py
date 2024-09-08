from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the global and current sum
        globalsum = nums[0]
        currsum = nums[0]
        
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # Update currsum to either the current element or currsum + current element
            currsum = max(nums[i], currsum + nums[i])
            # Update globalsum if currsum is greater
            globalsum = max(globalsum, currsum)
        
        return globalsum