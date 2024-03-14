class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        allmax = 0
        for i in accounts:
            m = 0
            for j in i:
                m += j
                allmax = max(allmax, m)
        return allmax