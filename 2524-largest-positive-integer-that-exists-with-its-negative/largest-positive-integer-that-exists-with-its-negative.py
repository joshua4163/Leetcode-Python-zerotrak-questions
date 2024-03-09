class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = -1
        x = set(nums)
        for i in nums:
            if -i in x:
                m = max(m, abs(i))
        return m if m != -1 else -1