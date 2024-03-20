class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l =[]
        c = sum(x for x in nums if x % 2 == 0)
        for val1,val2 in queries:
            if nums[val2] % 2 == 0:
                c -= nums[val2]
            nums[val2] += val1
            if nums[val2] % 2 == 0:
                c += nums[val2]
            l.append(c)
        return l