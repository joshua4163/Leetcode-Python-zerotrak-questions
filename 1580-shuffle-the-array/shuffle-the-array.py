class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        for i in range(n):
            l += [nums[i],nums[i+n]]
        return l
        