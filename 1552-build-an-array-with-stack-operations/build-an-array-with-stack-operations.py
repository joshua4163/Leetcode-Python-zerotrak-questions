class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        newtarget = set(target)
        l = []
        for i in range(1,target[-1]+1):
            if i in target:
                l.append("Push")
            else:
                l.append("Push")
                l.append("Pop")
        return l