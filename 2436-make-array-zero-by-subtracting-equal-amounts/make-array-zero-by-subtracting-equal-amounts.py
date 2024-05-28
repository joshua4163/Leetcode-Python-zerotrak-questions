class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
    # Initialize a min-heap
        heap = []
        for num in nums:
            if num > 0:
                heapq.heappush(heap, num)
    
    # To store the number of operations needed
        operations = 0
    
        while heap:
        # Extract the smallest element
            min_val = heapq.heappop(heap)
        # Increase operation count
            operations += 1
        # Skip all the elements equal to the min_val
            while heap and heap[0] == min_val:
                heapq.heappop(heap)
    
        return operations