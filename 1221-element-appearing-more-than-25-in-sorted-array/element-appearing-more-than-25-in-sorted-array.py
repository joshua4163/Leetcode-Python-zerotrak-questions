class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashmap = {}
        n = len(arr)
        for i in range(len(arr)):
            hashmap[arr[i]] = 1 + hashmap.get(arr[i],0)
            if hashmap[arr[i]] > n / 4:
                return arr[i]