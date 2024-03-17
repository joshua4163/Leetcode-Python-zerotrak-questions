class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = []
        hashmap = {}
        for i in arr1:
            hashmap[i] = hashmap.get(i,0) + 1
        # key(arr1 values)-value(howmany times it got repeated) = 1-1,2-3,3-2,4-1,6-1,7-1,9-1,19-1
        for j in arr2:
            if j in hashmap:
                l.extend([j] * hashmap[j])
                del hashmap[j]
        for k in sorted(hashmap):
            if k not in l:
                l.extend([k] * hashmap[k])
        return l