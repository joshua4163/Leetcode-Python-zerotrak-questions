class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        unique = set()
        for count in hashmap.values():
            if count in unique:
                return False
            unique.add(count)
        return True
