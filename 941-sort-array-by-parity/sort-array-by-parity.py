class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                l.append(nums[i])
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                l.append(nums[j])
        return l