class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sums = nums[-1]
        nums[-1] += 1
        for i in range(k - 1):
            sums += nums[-1]
            nums[-1] += 1
        return sums