from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute Force
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in res:
                            res.append(triplet)
        
        return res
        '''
        #Optimal
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            l = i + 1
            r = n - 1
            while l<r:
                summ = nums[l] + nums[r]
                diff = summ + nums[i]
                if diff == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+= 1
                    r-= 1
                elif diff < 0:
                    l+= 1
                else:
                    r -= 1
        # Convert the set of tuples to a list of lists
        return [list(triplets) for triplets in res]