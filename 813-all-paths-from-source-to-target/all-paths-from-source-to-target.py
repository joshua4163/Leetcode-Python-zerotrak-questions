class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        n = len(graph)
        
        def solve(current, res):
            if current == n-1:
                self.result.append(res.copy())
                return

            for node in graph[current]:
                res.append(node)
                solve(node, res)
                res.pop()

        solve(0,[0])
        return self.result