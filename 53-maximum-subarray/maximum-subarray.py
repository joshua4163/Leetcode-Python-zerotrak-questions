class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        temp = 0
        for i in nums:
            temp += i 
            maxi = max(maxi,temp)
            temp = 0 if temp <0 else temp
        return maxi