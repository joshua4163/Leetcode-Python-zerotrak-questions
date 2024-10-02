class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        hashmap = {}

        #assign ranking
        for i in range(len(sorted_arr)):
            hashmap[sorted_arr[i]] = i + 1

        #replace
        for i in range(len(arr)):
            arr[i] = hashmap[arr[i]]
        
        return arr