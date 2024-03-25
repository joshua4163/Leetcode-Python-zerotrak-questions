class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        l = []
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        for key,value in hashmap.items():
            if value == 2:
                l.append(key)
        return l