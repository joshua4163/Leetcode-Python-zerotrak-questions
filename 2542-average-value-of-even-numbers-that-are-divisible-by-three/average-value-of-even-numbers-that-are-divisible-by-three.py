class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # Initialize variables to keep track of total and count
        total = 0
        count = 0
        
        # Iterate through the list of numbers
        for i in range(len(nums)):
            # Check if the number is both divisible by 3 and even
            if nums[i] % 3 == 0 and nums[i] % 2 == 0:
                # Increment count and add the number to total
                count += 1
                total += nums[i]
        
        # If no numbers satisfy the condition, return 0 to avoid division by zero
        if count == 0:
            return 0
        
        # Calculate and return the average
        return int(total / count)
