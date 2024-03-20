class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # we are setting mindiff as infinity
        mindif  = math.inf
        #using def dic output: {'fruits': ['apple']})
        dic = collections.defaultdict(list)
        #sorting
        arr.sort()                         
        #to not go out of index we are using len -1
        for i in range(len(arr)-1):
            diff = arr[i+1] -arr[i]
            dic[diff].append([arr[i],arr[i+1]])
            mindif = min(mindif,diff)
        return dic[mindif]