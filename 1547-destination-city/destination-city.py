class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = {}
        ongoing = {}

        for i in paths:
            outgoing[i[0]] = outgoing.get(i[0], 0) + 1
            ongoing[i[1]] = ongoing.get(i[1], 0) + 1

        for city,count in ongoing.items():
            if count == 1 and outgoing.get(city,0)==0:
                return city