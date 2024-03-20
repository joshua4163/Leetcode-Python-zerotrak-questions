class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg=0
        pos=0
        for i in nums:
            if i>0:
                pos+=1
            if i<0:
                neg+=1

        return pos if pos > neg else neg