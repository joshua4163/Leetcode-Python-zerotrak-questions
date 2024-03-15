class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        pairs = 0
        leftover = 0
        for j in hashmap.values():
            pairs += j // 2
            leftover += j % 2
        return [pairs,leftover]