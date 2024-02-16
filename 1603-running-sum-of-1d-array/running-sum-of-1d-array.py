class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        result = 0
        for i in range(len(nums)):
            result = result + nums[i]
            l.append(result)
        return l