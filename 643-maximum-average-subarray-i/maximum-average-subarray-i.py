class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the initial sum of the first k elements
        max_sum = sum(nums[:k])
        current_sum = max_sum
        
        # Slide the window and update the max_sum if a larger sum is found
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / k