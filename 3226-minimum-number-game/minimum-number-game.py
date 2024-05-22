class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapq.heapify(nums)
        arr = []
        while nums:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            arr.append(n2)
            arr.append(n1)
        return arr